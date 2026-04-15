import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_approval_decision(patient_info, requested_service, service_price=0):
    covered_services = patient_info.get("covered_services", {})
    service_coverage = covered_services.get(requested_service)

    if service_coverage:
        coverage_str = json.dumps(service_coverage, indent=2)
    else:
        coverage_str = "Service not listed in policy schedule. Treat as Not Covered unless it falls under general medical necessity."

    pre_auth_required = patient_info.get("pre_auth_required", False)
    pre_auth_limit = patient_info.get("pre_auth_limit")

    if service_price > 0:
        price_context = "SR " + "{:,.2f}".format(service_price)
    else:
        price_context = "Not provided"

    if pre_auth_required and service_price > 0 and pre_auth_limit:
        if service_price > pre_auth_limit:
            pa_flag = ("ALERT: Price (" + price_context + ") exceeds pre-auth threshold "
                       "(SR " + "{:,}".format(pre_auth_limit) + "). Pre-authorization is REQUIRED.")
        else:
            pa_flag = ("Price (" + price_context + ") is below pre-auth threshold "
                       "(SR " + "{:,}".format(pre_auth_limit) + "). Pre-auth not triggered by price alone.")
    elif pre_auth_required:
        pa_flag = "Pre-authorization is required for ALL services under this member class."
    else:
        pa_flag = "No pre-authorization required for this member class."

    history_items = patient_info.get("medical_history", [])
    history_parts = []
    for h in history_items:
        history_parts.append(h["condition"] + " (" + h["status"] + "): " + h["notes"])
    history_str = "; ".join(history_parts) if history_parts else "None recorded"

    chronic = patient_info.get("chronic_conditions", [])
    allergies = patient_info.get("allergies", [])

    prompt = (
        "You are a senior Medical Insurance Auditor. Analyze this approval request.\n\n"
        "=== PATIENT ===\n"
        "ID: " + str(patient_info.get("id")) + "\n"
        "Name: " + str(patient_info.get("name")) + "\n"
        "DOB: " + str(patient_info.get("dob")) + " | Gender: " + str(patient_info.get("gender")) + "\n"
        "Chronic Conditions: " + (", ".join(chronic) if chronic else "None") + "\n"
        "Allergies: " + (", ".join(allergies) if allergies else "None") + "\n"
        "Medical History: " + history_str + "\n\n"
        "=== POLICY ===\n"
        "Policy: " + str(patient_info.get("policy_number")) + " | Insurer: " + str(patient_info.get("insurance_company")) + "\n"
        "Holder: " + str(patient_info.get("policy_holder")) + " | Validity: " + str(patient_info.get("policy_effective")) + "\n"
        "Member Class: " + str(patient_info.get("class")) + " | Annual Limit: SR " + "{:,}".format(patient_info.get("limits", 0)) + "\n"
        "Accommodation: " + str(patient_info.get("accommodation")) + "\n"
        "Coverage Type: " + str(patient_info.get("coverage")) + "\n"
        "Outpatient Deductible: " + str(patient_info.get("outpatient_deductible")) + "\n"
        "Network: " + str(patient_info.get("network")) + "\n"
        "Special Instructions: " + str(patient_info.get("special_instructions")) + "\n\n"
        "=== PRE-AUTHORIZATION ===\n"
        + pa_flag + "\n"
        "Notes: " + str(patient_info.get("pre_auth_notes")) + "\n\n"
        "=== REQUESTED SERVICE ===\n"
        "Service: " + requested_service + "\n"
        "Price: " + price_context + "\n\n"
        "=== POLICY COVERAGE FOR THIS SERVICE ===\n"
        + coverage_str + "\n\n"
        "=== INSTRUCTIONS ===\n"
        "1. Verify if the service is covered and check any sub-limits.\n"
        "2. Determine if pre-auth is required (class rules AND price threshold).\n"
        "3. Consider if the patient medical history supports medical necessity.\n"
        "4. Set status: Approved, Not Approved, or Pre-Auth Required.\n"
        "5. hospital_reason: Formal, detailed. Reference policy, sub-limits, pre-auth triggers, medical history.\n"
        "6. patient_reason: Simple and empathetic. What is covered, what they need to do, why.\n\n"
        'Return ONLY valid JSON (no markdown, no preamble):\n'
        '{"status": "...", "hospital_reason": "...", "patient_reason": "..."}'
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={"response_mime_type": "application/json"}
        )
        text = response.text.strip()
        if text.startswith("```"):
            parts = text.split("```")
            text = parts[1] if len(parts) > 1 else text
            if text.startswith("json"):
                text = text[4:]
        return json.loads(text.strip())
    except Exception as e:
        return {
            "status": "Error",
            "patient_reason": "Analysis could not be completed. Please try again.",
            "hospital_reason": "LLM generation failed: " + str(e)
        }