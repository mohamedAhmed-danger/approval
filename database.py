# ─────────────────────────────────────────────
#  REVY AI  —  Demo Database
#  Separated: Companies → Policies → Patients
# ─────────────────────────────────────────────

INSURANCE_COMPANIES = {
    "IHC": {
        "id": "IHC",
        "name": "International Health Company",
        "country": "Saudi Arabia",
        "network": "IHC National Network",
        "contact": "+966-11-000-1001"
    },
    "BUPA": {
        "id": "BUPA",
        "name": "Bupa Arabia",
        "country": "Saudi Arabia",
        "network": "Bupa Premium Network",
        "contact": "+966-11-000-2002"
    },
    "TAWUNIYA": {
        "id": "TAWUNIYA",
        "name": "Al-Tawuniya Insurance",
        "country": "Saudi Arabia",
        "network": "Tawuniya National Network",
        "contact": "+966-11-000-3003"
    }
}

POLICIES = {
    "502277005": {
        "policy_number": "502277005",
        "company_id": "IHC",
        "company_name": "International Health Company",
        "policy_holder": "IHP ARA International Media Production",
        "effective_from": "2025-02-01",
        "effective_to": "2026-01-31",
        "classes": {
            "VIP": {
                "annual_limit": 1875000,
                "accommodation": "Standard Suite",
                "inpatient": True,
                "outpatient": True,
                "outpatient_deductible": "20% up to SR 50",
                "pre_auth_required": False,
                "pre_auth_limit": None,
                "pre_auth_notes": "No pre-authorization required for VIP members (inpatient or outpatient). Medication limit equals approval limit.",
                "covered_services": {
                    "MRI Scan": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "CT Scan": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "X-Ray": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Blood Test": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Ultrasound": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Physiotherapy": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "General Surgery": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Laparoscopic Surgery": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Maternity": {"covered": True, "limit": "SR 30,000", "notes": ""},
                    "Dental (Corrective)": {"covered": True, "limit": "SR 3,000", "notes": "0% deductible"},
                    "Dental (Emergency)": {"covered": True, "limit": "SR 2,000", "notes": "20% up to SR 800"},
                    "Dental (General)": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Optical": {"covered": True, "limit": "SR 2,250", "notes": "Frame SR 800 sub-limit"},
                    "Vaccination": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Psychiatric": {"covered": True, "limit": "SR 50,000", "notes": ""},
                    "Dialysis": {"covered": True, "limit": "SR 180,000", "notes": ""},
                    "Hearing Aids": {"covered": True, "limit": "SR 6,000", "notes": ""},
                    "Kidney Transplant": {"covered": True, "limit": "SR 250,000", "notes": ""},
                    "Bone Marrow Transplant": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Obesity Surgery": {"covered": True, "limit": "SR 20,000", "notes": "BMI > 35 required"},
                    "ABA Therapy": {"covered": True, "limit": "SR 50,000", "notes": "Per CHI regulations"},
                    "Cancer Treatment": {"covered": True, "limit": "Annual Limit", "notes": "Includes wig SR 1,000"},
                    "Routine Checkup": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Screening": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Birth Control": {"covered": True, "limit": "SR 1,500", "notes": ""},
                    "Circumcision": {"covered": True, "limit": "SR 500", "notes": ""},
                    "Neonatal Care": {"covered": True, "limit": "Annual Limit", "notes": ""},
                },
                "special_instructions": "Autism/ABA: SR 50,000 (CHI). Down Syndrome: Covered. Cancer + wig SR 1,000. Supplements/Probiotics: Covered. Glucometers: Covered. Joint Replacement: 3 members. Vision Correction: 5 members."
            },
            "A": {
                "annual_limit": 1875000,
                "accommodation": "Single Room",
                "inpatient": True,
                "outpatient": True,
                "outpatient_deductible": "20% up to SR 50",
                "pre_auth_required": True,
                "pre_auth_limit": 2500,
                "pre_auth_notes": "Pre-authorization required for services exceeding SR 2,500. Medication limit equals approval limit.",
                "covered_services": {
                    "MRI Scan": {"covered": True, "limit": "Annual Limit", "notes": "Pre-auth if > SR 2,500"},
                    "CT Scan": {"covered": True, "limit": "Annual Limit", "notes": "Pre-auth if > SR 2,500"},
                    "X-Ray": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Blood Test": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Ultrasound": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Physiotherapy": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "General Surgery": {"covered": True, "limit": "Annual Limit", "notes": "Pre-auth required"},
                    "Laparoscopic Surgery": {"covered": True, "limit": "Annual Limit", "notes": "Pre-auth required"},
                    "Maternity": {"covered": True, "limit": "SR 30,000", "notes": ""},
                    "Dental (Corrective)": {"covered": True, "limit": "SR 3,000", "notes": "0% deductible"},
                    "Dental (Emergency)": {"covered": True, "limit": "SR 2,000", "notes": "20% up to SR 800"},
                    "Dental (General)": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Optical": {"covered": True, "limit": "SR 2,250", "notes": "Frame SR 800 sub-limit"},
                    "Vaccination": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Psychiatric": {"covered": True, "limit": "SR 50,000", "notes": ""},
                    "Dialysis": {"covered": True, "limit": "SR 180,000", "notes": ""},
                    "Hearing Aids": {"covered": True, "limit": "SR 6,000", "notes": ""},
                    "Kidney Transplant": {"covered": True, "limit": "SR 250,000", "notes": "Pre-auth required"},
                    "Bone Marrow Transplant": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Obesity Surgery": {"covered": True, "limit": "SR 20,000", "notes": "BMI > 35, pre-auth required"},
                    "ABA Therapy": {"covered": True, "limit": "SR 50,000", "notes": "Per CHI regulations"},
                    "Cancer Treatment": {"covered": True, "limit": "Annual Limit", "notes": "Includes wig SR 1,000"},
                    "Routine Checkup": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Screening": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Birth Control": {"covered": True, "limit": "SR 1,500", "notes": ""},
                    "Circumcision": {"covered": True, "limit": "SR 500", "notes": ""},
                    "Neonatal Care": {"covered": True, "limit": "Annual Limit", "notes": ""},
                },
                "special_instructions": "Autism/ABA: SR 50,000 (CHI). Down Syndrome: Covered. Cancer + wig SR 1,000. Supplements/Probiotics: Covered. Glucometers: Covered. Joint Replacement: 3 members. Vision Correction: 5 members."
            }
        }
    },
    "BUPA-ENT-2025": {
        "policy_number": "BUPA-ENT-2025",
        "company_id": "BUPA",
        "company_name": "Bupa Arabia",
        "policy_holder": "Al-Faris Technology Solutions",
        "effective_from": "2025-01-01",
        "effective_to": "2025-12-31",
        "classes": {
            "PLATINUM": {
                "annual_limit": 2000000,
                "accommodation": "VIP Suite",
                "inpatient": True,
                "outpatient": True,
                "outpatient_deductible": "10% up to SR 30",
                "pre_auth_required": False,
                "pre_auth_limit": None,
                "pre_auth_notes": "No pre-authorization required for Platinum members.",
                "covered_services": {
                    "MRI Scan": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "CT Scan": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "X-Ray": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Blood Test": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Ultrasound": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Physiotherapy": {"covered": True, "limit": "SR 80,000", "notes": ""},
                    "General Surgery": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Laparoscopic Surgery": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Maternity": {"covered": True, "limit": "SR 50,000", "notes": ""},
                    "Dental (Corrective)": {"covered": True, "limit": "SR 5,000", "notes": ""},
                    "Dental (Emergency)": {"covered": True, "limit": "SR 3,000", "notes": ""},
                    "Dental (General)": {"covered": True, "limit": "SR 2,000", "notes": "Annual"},
                    "Optical": {"covered": True, "limit": "SR 3,000", "notes": ""},
                    "Vaccination": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Psychiatric": {"covered": True, "limit": "SR 75,000", "notes": ""},
                    "Dialysis": {"covered": True, "limit": "SR 200,000", "notes": ""},
                    "Hearing Aids": {"covered": True, "limit": "SR 8,000", "notes": ""},
                    "Kidney Transplant": {"covered": True, "limit": "SR 300,000", "notes": ""},
                    "Bone Marrow Transplant": {"covered": True, "limit": "SR 200,000", "notes": ""},
                    "Obesity Surgery": {"covered": True, "limit": "SR 30,000", "notes": "BMI > 30"},
                    "ABA Therapy": {"covered": True, "limit": "SR 60,000", "notes": ""},
                    "Cancer Treatment": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Routine Checkup": {"covered": True, "limit": "SR 2,000", "notes": "Annual"},
                    "Screening": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Birth Control": {"covered": True, "limit": "SR 2,000", "notes": ""},
                    "Circumcision": {"covered": True, "limit": "SR 800", "notes": ""},
                    "Neonatal Care": {"covered": True, "limit": "Annual Limit", "notes": ""},
                },
                "special_instructions": "International coverage up to SR 500,000. Second opinion service available. Wellness programs covered."
            },
            "GOLD": {
                "annual_limit": 750000,
                "accommodation": "Single Room",
                "inpatient": True,
                "outpatient": True,
                "outpatient_deductible": "20% up to SR 50",
                "pre_auth_required": True,
                "pre_auth_limit": 3000,
                "pre_auth_notes": "Pre-authorization required for services exceeding SR 3,000.",
                "covered_services": {
                    "MRI Scan": {"covered": True, "limit": "Annual Limit", "notes": "Pre-auth if > SR 3,000"},
                    "CT Scan": {"covered": True, "limit": "Annual Limit", "notes": "Pre-auth if > SR 3,000"},
                    "X-Ray": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Blood Test": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Ultrasound": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Physiotherapy": {"covered": True, "limit": "SR 30,000", "notes": ""},
                    "General Surgery": {"covered": True, "limit": "Annual Limit", "notes": "Pre-auth required"},
                    "Laparoscopic Surgery": {"covered": True, "limit": "Annual Limit", "notes": "Pre-auth required"},
                    "Maternity": {"covered": True, "limit": "SR 25,000", "notes": ""},
                    "Dental (Corrective)": {"covered": True, "limit": "SR 2,500", "notes": ""},
                    "Dental (Emergency)": {"covered": True, "limit": "SR 1,500", "notes": ""},
                    "Dental (General)": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Optical": {"covered": True, "limit": "SR 1,500", "notes": ""},
                    "Vaccination": {"covered": True, "limit": "SR 1,000", "notes": ""},
                    "Psychiatric": {"covered": True, "limit": "SR 30,000", "notes": ""},
                    "Dialysis": {"covered": True, "limit": "SR 120,000", "notes": ""},
                    "Hearing Aids": {"covered": True, "limit": "SR 4,000", "notes": ""},
                    "Kidney Transplant": {"covered": True, "limit": "SR 200,000", "notes": ""},
                    "Bone Marrow Transplant": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Obesity Surgery": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "ABA Therapy": {"covered": True, "limit": "SR 40,000", "notes": ""},
                    "Cancer Treatment": {"covered": True, "limit": "SR 400,000", "notes": ""},
                    "Routine Checkup": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Screening": {"covered": True, "limit": "SR 5,000", "notes": ""},
                    "Birth Control": {"covered": True, "limit": "SR 1,000", "notes": ""},
                    "Circumcision": {"covered": True, "limit": "SR 500", "notes": ""},
                    "Neonatal Care": {"covered": True, "limit": "SR 50,000", "notes": ""},
                },
                "special_instructions": "Dental general not covered. Obesity surgery excluded. Bone marrow excluded."
            }
        }
    },
    "TAW-SME-2025": {
        "policy_number": "TAW-SME-2025",
        "company_id": "TAWUNIYA",
        "company_name": "Al-Tawuniya Insurance",
        "policy_holder": "Green Horizon Trading Co.",
        "effective_from": "2025-03-01",
        "effective_to": "2026-02-28",
        "classes": {
            "B": {
                "annual_limit": 300000,
                "accommodation": "Semi-Private Room",
                "inpatient": True,
                "outpatient": True,
                "outpatient_deductible": "20% up to SR 60",
                "pre_auth_required": True,
                "pre_auth_limit": 1500,
                "pre_auth_notes": "Pre-authorization required for all services exceeding SR 1,500 or any inpatient admission.",
                "covered_services": {
                    "MRI Scan": {"covered": True, "limit": "SR 5,000/scan", "notes": "Pre-auth required"},
                    "CT Scan": {"covered": True, "limit": "SR 3,000/scan", "notes": "Pre-auth required"},
                    "X-Ray": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Blood Test": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Ultrasound": {"covered": True, "limit": "Annual Limit", "notes": ""},
                    "Physiotherapy": {"covered": True, "limit": "SR 10,000", "notes": "Max 20 sessions/year"},
                    "General Surgery": {"covered": True, "limit": "Annual Limit", "notes": "Pre-auth required"},
                    "Laparoscopic Surgery": {"covered": True, "limit": "Annual Limit", "notes": "Pre-auth required"},
                    "Maternity": {"covered": True, "limit": "SR 15,000", "notes": "Normal delivery only"},
                    "Dental (Corrective)": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Dental (Emergency)": {"covered": True, "limit": "SR 1,000", "notes": ""},
                    "Dental (General)": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Optical": {"covered": True, "limit": "SR 800", "notes": "Every 2 years"},
                    "Vaccination": {"covered": True, "limit": "SR 500", "notes": "Children only"},
                    "Psychiatric": {"covered": True, "limit": "SR 15,000", "notes": ""},
                    "Dialysis": {"covered": True, "limit": "SR 80,000", "notes": ""},
                    "Hearing Aids": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Kidney Transplant": {"covered": True, "limit": "SR 150,000", "notes": "Pre-auth required"},
                    "Bone Marrow Transplant": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Obesity Surgery": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "ABA Therapy": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Cancer Treatment": {"covered": True, "limit": "SR 200,000", "notes": "Pre-auth required"},
                    "Routine Checkup": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Screening": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Birth Control": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Circumcision": {"covered": True, "limit": "SR 300", "notes": ""},
                    "Neonatal Care": {"covered": True, "limit": "SR 30,000", "notes": ""},
                },
                "special_instructions": "Network hospitals only. Referral letter required for specialists. No international coverage."
            },
            "C": {
                "annual_limit": 50000,
                "accommodation": "Shared Ward",
                "inpatient": True,
                "outpatient": False,
                "outpatient_deductible": "30% up to SR 100",
                "pre_auth_required": True,
                "pre_auth_limit": 500,
                "pre_auth_notes": "Pre-authorization required for ALL services. Outpatient not covered under this class.",
                "covered_services": {
                    "MRI Scan": {"covered": True, "limit": "SR 2,000", "notes": "Inpatient only, pre-auth required"},
                    "CT Scan": {"covered": True, "limit": "SR 1,500", "notes": "Inpatient only"},
                    "X-Ray": {"covered": True, "limit": "SR 500", "notes": ""},
                    "Blood Test": {"covered": True, "limit": "SR 200", "notes": ""},
                    "Ultrasound": {"covered": True, "limit": "SR 500", "notes": ""},
                    "Physiotherapy": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "General Surgery": {"covered": True, "limit": "Annual Limit", "notes": "Emergency only"},
                    "Laparoscopic Surgery": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Maternity": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Dental (Corrective)": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Dental (Emergency)": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Dental (General)": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Optical": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Vaccination": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Psychiatric": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Dialysis": {"covered": True, "limit": "SR 30,000", "notes": ""},
                    "Hearing Aids": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Kidney Transplant": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Bone Marrow Transplant": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Obesity Surgery": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "ABA Therapy": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Cancer Treatment": {"covered": True, "limit": "SR 50,000", "notes": "Inpatient only"},
                    "Routine Checkup": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Screening": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Birth Control": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Circumcision": {"covered": False, "limit": "Not Covered", "notes": ""},
                    "Neonatal Care": {"covered": False, "limit": "Not Covered", "notes": ""},
                },
                "special_instructions": "Emergency inpatient admissions only. All non-emergency services require prior approval from Tawuniya medical team."
            }
        }
    }
}

PATIENTS = {
    "P1001": {
        "id": "P1001",
        "name": "Ahmed Youssef Al-Harbi",
        "dob": "1985-06-15",
        "gender": "Male",
        "nationality": "Saudi",
        "policy_number": "502277005",
        "policy_class": "A",
        "medical_history": [
            {"condition": "Hypertension", "diagnosed": "2019", "status": "Managed", "notes": "Amlodipine 5mg daily"},
            {"condition": "Appendectomy", "diagnosed": "2024-03", "status": "Resolved", "notes": "Laparoscopic, no complications"},
            {"condition": "Pre-diabetes", "diagnosed": "2022", "status": "Monitored", "notes": "HbA1c: 6.1%"},
        ],
        "allergies": ["Penicillin"],
        "chronic_conditions": ["Hypertension"],
        "last_visit": "2025-11-20"
    },
    "P1002": {
        "id": "P1002",
        "name": "Sarah Khalid Mansour",
        "dob": "1992-03-28",
        "gender": "Female",
        "nationality": "Saudi",
        "policy_number": "TAW-SME-2025",
        "policy_class": "B",
        "medical_history": [
            {"condition": "Asthma", "diagnosed": "2005", "status": "Chronic", "notes": "Salbutamol inhaler PRN, Seretide daily"},
            {"condition": "Seasonal Allergic Rhinitis", "diagnosed": "2010", "status": "Seasonal", "notes": "Cetirizine spring/fall"},
        ],
        "allergies": ["Aspirin", "NSAIDs"],
        "chronic_conditions": ["Asthma"],
        "last_visit": "2025-10-05"
    },
    "P1003": {
        "id": "P1003",
        "name": "Khaled Ibrahim Al-Rashid",
        "dob": "1978-11-02",
        "gender": "Male",
        "nationality": "Saudi",
        "policy_number": "502277005",
        "policy_class": "VIP",
        "medical_history": [
            {"condition": "Type 2 Diabetes Mellitus", "diagnosed": "2015", "status": "Chronic", "notes": "Metformin 1000mg + Januvia. HbA1c: 7.4%"},
            {"condition": "Hypercholesterolemia", "diagnosed": "2017", "status": "Managed", "notes": "Atorvastatin 40mg. LDL: 2.1 mmol/L"},
            {"condition": "Diabetic Nephropathy Stage 2", "diagnosed": "2023", "status": "Monitored", "notes": "eGFR: 68. Annual nephrology review"},
        ],
        "allergies": ["Sulfa drugs"],
        "chronic_conditions": ["Type 2 Diabetes", "Hypercholesterolemia", "Diabetic Nephropathy"],
        "last_visit": "2025-12-01"
    },
    "P1004": {
        "id": "P1004",
        "name": "Fatima Mohammed Al-Zahra",
        "dob": "1995-07-19",
        "gender": "Female",
        "nationality": "Saudi",
        "policy_number": "BUPA-ENT-2025",
        "policy_class": "PLATINUM",
        "medical_history": [
            {"condition": "Polycystic Ovary Syndrome (PCOS)", "diagnosed": "2018", "status": "Managed", "notes": "Metformin 500mg, Spironolactone"},
            {"condition": "Iron Deficiency Anemia", "diagnosed": "2023", "status": "Treated", "notes": "Ferrous sulfate ongoing"},
            {"condition": "Generalized Anxiety Disorder", "diagnosed": "2021", "status": "Managed", "notes": "CBT therapy, no medication"},
        ],
        "allergies": [],
        "chronic_conditions": ["PCOS", "Anxiety Disorder"],
        "last_visit": "2025-11-10"
    },
    "P1005": {
        "id": "P1005",
        "name": "Omar Saeed Al-Dosari",
        "dob": "1960-01-30",
        "gender": "Male",
        "nationality": "Saudi",
        "policy_number": "502277005",
        "policy_class": "A",
        "medical_history": [
            {"condition": "Coronary Artery Disease", "diagnosed": "2018", "status": "Managed", "notes": "Stent placed 2018. Dual antiplatelet therapy"},
            {"condition": "Heart Failure (NYHA II)", "diagnosed": "2022", "status": "Chronic", "notes": "EF: 40%. Bisoprolol, Furosemide, Sacubitril"},
            {"condition": "Chronic Kidney Disease Stage 3", "diagnosed": "2023", "status": "Monitored", "notes": "eGFR: 42. Nephrology every 3 months"},
            {"condition": "Atrial Fibrillation", "diagnosed": "2020", "status": "Managed", "notes": "Apixaban. Rate-controlled"},
        ],
        "allergies": ["Contrast dye (relative)"],
        "chronic_conditions": ["CAD", "Heart Failure", "CKD Stage 3", "Atrial Fibrillation"],
        "last_visit": "2025-12-10"
    },
    "P1006": {
        "id": "P1006",
        "name": "Layla Hassan Al-Otaibi",
        "dob": "1988-09-14",
        "gender": "Female",
        "nationality": "Saudi",
        "policy_number": "BUPA-ENT-2025",
        "policy_class": "GOLD",
        "medical_history": [
            {"condition": "Rheumatoid Arthritis", "diagnosed": "2016", "status": "Chronic", "notes": "Methotrexate 15mg weekly. Moderate activity"},
            {"condition": "Osteoporosis (early)", "diagnosed": "2024", "status": "Monitored", "notes": "DEXA: -2.1. Vitamin D + Calcium"},
        ],
        "allergies": ["Ibuprofen"],
        "chronic_conditions": ["Rheumatoid Arthritis", "Osteoporosis"],
        "last_visit": "2025-10-22"
    },
    "P1007": {
        "id": "P1007",
        "name": "Yusuf Tariq Al-Ghamdi",
        "dob": "2010-04-03",
        "gender": "Male",
        "nationality": "Saudi",
        "policy_number": "502277005",
        "policy_class": "VIP",
        "medical_history": [
            {"condition": "Autism Spectrum Disorder (Level 2)", "diagnosed": "2013", "status": "Ongoing", "notes": "ABA therapy 20hrs/week. Speech therapy weekly"},
            {"condition": "ADHD", "diagnosed": "2015", "status": "Managed", "notes": "Methylphenidate 10mg AM. Behavioral therapy"},
            {"condition": "Epilepsy (controlled)", "diagnosed": "2014", "status": "Controlled", "notes": "Valproate 500mg BD. Seizure-free 2 years"},
        ],
        "allergies": [],
        "chronic_conditions": ["ASD Level 2", "ADHD", "Epilepsy"],
        "last_visit": "2025-11-28"
    },
    "P1008": {
        "id": "P1008",
        "name": "Nora Abdullah Al-Shehri",
        "dob": "1970-12-22",
        "gender": "Female",
        "nationality": "Saudi",
        "policy_number": "TAW-SME-2025",
        "policy_class": "C",
        "medical_history": [
            {"condition": "End-Stage Renal Disease (ESRD)", "diagnosed": "2021", "status": "Active", "notes": "Hemodialysis 3x/week. Transplant list evaluation"},
            {"condition": "Anemia of Chronic Disease", "diagnosed": "2021", "status": "Managed", "notes": "Erythropoietin injections. Hb: 9.2 g/dL"},
            {"condition": "Secondary Hypertension", "diagnosed": "2019", "status": "Managed", "notes": "Amlodipine + Ramipril"},
        ],
        "allergies": ["Codeine"],
        "chronic_conditions": ["ESRD", "Anemia", "Hypertension"],
        "last_visit": "2025-12-08"
    }
}

ALL_SERVICES = sorted([
    "MRI Scan", "CT Scan", "X-Ray", "Blood Test", "Ultrasound",
    "Physiotherapy", "General Surgery", "Laparoscopic Surgery",
    "Maternity", "Dental (Corrective)", "Dental (Emergency)", "Dental (General)",
    "Optical", "Vaccination", "Psychiatric", "Dialysis", "Hearing Aids",
    "Kidney Transplant", "Bone Marrow Transplant", "Obesity Surgery",
    "ABA Therapy", "Cancer Treatment", "Routine Checkup", "Screening",
    "Birth Control", "Circumcision", "Neonatal Care",
])


def get_patient_data(patient_id):
    patient = PATIENTS.get(patient_id.upper())
    if not patient:
        return None
    policy = POLICIES.get(patient["policy_number"])
    if not policy:
        return None
    cls = patient["policy_class"]
    class_data = policy["classes"].get(cls)
    if not class_data:
        return None
    company = INSURANCE_COMPANIES.get(policy["company_id"], {})
    return {
        "id": patient["id"],
        "name": patient["name"],
        "dob": patient["dob"],
        "gender": patient["gender"],
        "class": cls,
        "allergies": patient.get("allergies", []),
        "chronic_conditions": patient.get("chronic_conditions", []),
        "medical_history": patient.get("medical_history", []),
        "last_visit": patient.get("last_visit", "N/A"),
        "policy_number": patient["policy_number"],
        "policy_holder": policy["policy_holder"],
        "policy_effective": f"{policy['effective_from']} to {policy['effective_to']}",
        "insurance_company": company.get("name", policy["company_id"]),
        "network": company.get("network", "N/A"),
        "limits": class_data["annual_limit"],
        "accommodation": class_data["accommodation"],
        "coverage": "Inpatient + Outpatient" if class_data["inpatient"] and class_data["outpatient"] else "Inpatient Only",
        "outpatient_deductible": class_data["outpatient_deductible"],
        "pre_auth_required": class_data["pre_auth_required"],
        "pre_auth_limit": class_data.get("pre_auth_limit"),
        "pre_auth_notes": class_data["pre_auth_notes"],
        "covered_services": class_data["covered_services"],
        "special_instructions": class_data["special_instructions"],
    }


def get_all_patients():
    result = []
    for pid, p in PATIENTS.items():
        policy = POLICIES.get(p["policy_number"], {})
        company = INSURANCE_COMPANIES.get(policy.get("company_id", ""), {})
        result.append({
            "id": pid,
            "name": p["name"],
            "class": p["policy_class"],
            "insurance": company.get("name", ""),
            "policy_number": p["policy_number"],
        })
    return result


def get_services():
    return ALL_SERVICES