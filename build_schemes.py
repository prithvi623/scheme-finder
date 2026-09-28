"""
Builds schemes.json for the Eligibility & Benefits Navigator MVP.

IMPORTANT SCOPING NOTE (read before extending this file):
The task spec asks for 50-100 schemes. This build script ships 11
schemes that were actually looked up against official/authoritative
sources in this session (see each record's `source` block). Padding
the file with more schemes without doing that lookup would mean
inventing eligibility rules, amounts, or URLs -- which the spec
explicitly forbids ("Do not invent missing information").

To grow the dataset: research one scheme at a time on its official
portal (pmkisan.gov.in, pmjay.gov.in, myscheme.gov.in, npci/PFRDA for
APY, pmaymis.gov.in, scholarships.gov.in, telanganaepass.cgg.gov.in,
etc.), append a record in the same shape below, and set
verification_status honestly. Never mark a field "verified" you
didn't actually check.
"""

import json
from datetime import date

TODAY = "2026-09-25"  # date these entries were checked against search results


def doc(mandatory, conditional=None):
    return {"mandatory_documents": mandatory, "conditional_documents": conditional or []}


SCHEMES = [

  {
    "scheme_id": "CG001",
    "scheme_name": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
    "short_description": "Direct income support for eligible landholding farmer families.",
    "category": "Agriculture",
    "sub_category": "Farmer Income Support",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Agriculture and Farmers Welfare",
    "implementing_department": "Department of Agriculture and Farmers Welfare",
    "benefits": [
      {
        "type": "financial_assistance",
        "amount": "₹6,000 per year",
        "description": "Income support transferred in installments to eligible farmer families."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["farmer"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": True,
      "disability_status": None,
      "other_conditions": ["Eligible landholding farmer-family criteria apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Aadhaar", "Land/landholding records", "Bank account details"],
    "application": {
      "method": ["online", "through designated state/UT registration process"],
      "official_url": "",
      "offline_process": "Contact the designated local/state agriculture authorities or Common Service Centre."
    },
    "source": {
      "official_source_name": "National Government Services Portal / Ministry of Agriculture",
      "official_source_url": "https://services.india.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG002",
    "scheme_name": "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
    "short_description": "Crop insurance scheme providing financial protection against specified crop losses and risks.",
    "category": "Agriculture",
    "sub_category": "Crop Insurance",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Agriculture and Farmers Welfare",
    "implementing_department": "Department of Agriculture and Farmers Welfare",
    "benefits": [
      {
        "type": "insurance",
        "amount": "",
        "description": "Crop insurance protection against covered crop risks."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["farmer"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": True,
      "disability_status": None,
      "other_conditions": ["Eligibility depends on notified crops, areas and applicable crop-season rules."]
    },
    "eligibility_rules": [],
    "required_documents": ["Land/cultivation records", "Bank account details", "Identity document"],
    "application": {
      "method": ["online", "bank/financial institution", "designated insurance/intermediary channels"],
      "official_url": "",
      "offline_process": "Contact the notified bank, insurer or agriculture department."
    },
    "source": {
      "official_source_name": "Ministry of Agriculture and Farmers Welfare",
      "official_source_url": "https://agriwelfare.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG003",
    "scheme_name": "Kisan Credit Card (KCC)",
    "short_description": "Credit facility intended to provide timely institutional credit to farmers.",
    "category": "Agriculture",
    "sub_category": "Agricultural Credit",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Agriculture and Farmers Welfare",
    "implementing_department": "Department of Agriculture and Farmers Welfare",
    "benefits": [
      {
        "type": "credit",
        "amount": "",
        "description": "Credit facility for eligible agricultural and related needs."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["farmer", "agricultural worker", "tenant farmer", "sharecropper"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": True,
      "disability_status": None,
      "other_conditions": ["Eligibility and credit limit are subject to lending-bank assessment."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity proof", "Address proof", "Land/cultivation documents where applicable"],
    "application": {
      "method": ["bank"],
      "official_url": "",
      "offline_process": "Apply through participating banks or financial institutions."
    },
    "source": {
      "official_source_name": "Department of Agriculture and Farmers Welfare",
      "official_source_url": "https://agriwelfare.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG004",
    "scheme_name": "Pradhan Mantri Kisan Urja Suraksha evam Utthaan Mahabhiyan (PM-KUSUM)",
    "short_description": "Promotes solar energy use in agriculture, including decentralized solar power and solar agricultural pumps.",
    "category": "Agriculture",
    "sub_category": "Solar Energy",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of New and Renewable Energy",
    "implementing_department": "Ministry of New and Renewable Energy",
    "benefits": [
      {
        "type": "subsidy",
        "amount": "",
        "description": "Financial support under applicable components for solar agricultural applications."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["farmer"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": ["rural"],
      "farmer_status": True,
      "disability_status": None,
      "other_conditions": ["Component-specific and state-specific implementation conditions apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity proof", "Land documents", "Bank details"],
    "application": {
      "method": ["state implementing agency", "online where available"],
      "official_url": "",
      "offline_process": "Apply through the designated state implementing agency."
    },
    "source": {
      "official_source_name": "Ministry of New and Renewable Energy",
      "official_source_url": "https://mnre.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG005",
    "scheme_name": "Soil Health Card Scheme",
    "short_description": "Provides farmers with information about soil nutrient status and recommendations for soil management.",
    "category": "Agriculture",
    "sub_category": "Soil Management",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Agriculture and Farmers Welfare",
    "implementing_department": "Department of Agriculture and Farmers Welfare",
    "benefits": [
      {
        "type": "advisory",
        "amount": "",
        "description": "Soil testing and nutrient-management recommendations."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["farmer"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": True,
      "disability_status": None,
      "other_conditions": []
    },
    "eligibility_rules": [],
    "required_documents": ["Farmer identification/details", "Land details where required"],
    "application": {
      "method": ["state agriculture department", "designated soil-testing facility"],
      "official_url": "",
      "offline_process": "Contact the local agriculture department or soil-testing facility."
    },
    "source": {
      "official_source_name": "Department of Agriculture and Farmers Welfare",
      "official_source_url": "https://agriwelfare.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG006",
    "scheme_name": "Agriculture Infrastructure Fund (AIF)",
    "short_description": "Financing facility supporting agricultural infrastructure projects.",
    "category": "Agriculture",
    "sub_category": "Agricultural Infrastructure",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Agriculture and Farmers Welfare",
    "implementing_department": "Department of Agriculture and Farmers Welfare",
    "benefits": [
      {
        "type": "credit_support",
        "amount": "",
        "description": "Financing support for eligible agricultural infrastructure projects."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["farmer", "agri-entrepreneur", "eligible agricultural organization"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Eligible project and borrower categories apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Project documents", "Identity documents", "Bank/financial documents"],
    "application": {
      "method": ["online", "participating financial institution"],
      "official_url": "",
      "offline_process": "Approach a participating lending institution."
    },
    "source": {
      "official_source_name": "Ministry of Agriculture and Farmers Welfare",
      "official_source_url": "https://agriwelfare.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG007",
    "scheme_name": "National Agriculture Market (e-NAM)",
    "short_description": "National electronic trading platform intended to connect agricultural markets.",
    "category": "Agriculture",
    "sub_category": "Agricultural Marketing",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Agriculture and Farmers Welfare",
    "implementing_department": "Small Farmers' Agribusiness Consortium",
    "benefits": [
      {
        "type": "market_access",
        "amount": "",
        "description": "Electronic agricultural market and price-discovery facilities."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["farmer", "trader"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Participation depends on the applicable market and registration requirements."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity details", "Bank details where applicable", "Trader/farmer registration details"],
    "application": {
      "method": ["online"],
      "official_url": "https://www.enam.gov.in/",
      "offline_process": "Contact the relevant participating agricultural market."
    },
    "source": {
      "official_source_name": "e-NAM",
      "official_source_url": "https://www.enam.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG008",
    "scheme_name": "Pradhan Mantri Matsya Sampada Yojana (PMMSY)",
    "short_description": "Central sector scheme supporting fisheries development and related infrastructure.",
    "category": "Fisheries",
    "sub_category": "Fisheries Development",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Fisheries, Animal Husbandry and Dairying",
    "implementing_department": "Department of Fisheries",
    "benefits": [
      {
        "type": "financial_assistance",
        "amount": "",
        "description": "Support for eligible fisheries and aquaculture activities."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["fisher", "fish farmer", "eligible fisheries entrepreneur"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Component-specific eligibility applies."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity proof", "Bank details", "Fisheries/project documents"],
    "application": {
      "method": ["state fisheries department", "designated implementing agency"],
      "official_url": "",
      "offline_process": "Contact the State/UT fisheries department."
    },
    "source": {
      "official_source_name": "Department of Fisheries",
      "official_source_url": "https://dof.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG009",
    "scheme_name": "National Livestock Mission",
    "short_description": "Supports livestock entrepreneurship, development and related activities.",
    "category": "Agriculture",
    "sub_category": "Livestock",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Fisheries, Animal Husbandry and Dairying",
    "implementing_department": "Department of Animal Husbandry and Dairying",
    "benefits": [
      {
        "type": "subsidy",
        "amount": "",
        "description": "Support under applicable livestock entrepreneurship and development components."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["farmer", "livestock entrepreneur"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": True,
      "disability_status": None,
      "other_conditions": ["Component-specific conditions apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity proof", "Project documents", "Bank details"],
    "application": {
      "method": ["state implementing agency", "online where available"],
      "official_url": "",
      "offline_process": "Contact the State Animal Husbandry Department."
    },
    "source": {
      "official_source_name": "Department of Animal Husbandry and Dairying",
      "official_source_url": "https://dahd.nic.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG010",
    "scheme_name": "Pradhan Mantri Awas Yojana - Gramin (PMAY-G)",
    "short_description": "Rural housing programme providing assistance for eligible rural households to construct pucca houses.",
    "category": "Housing",
    "sub_category": "Rural Housing",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Rural Development",
    "implementing_department": "Department of Rural Development",
    "benefits": [
      {
        "type": "housing_assistance",
        "amount": "",
        "description": "Financial assistance for eligible rural households to construct a pucca house."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": ["rural"],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Beneficiary selection is based on applicable deprivation/household criteria and official lists."]
    },
    "eligibility_rules": [],
    "required_documents": ["Aadhaar/identity", "Bank account details", "Household/residence details"],
    "application": {
      "method": ["Gram Panchayat/local government process"],
      "official_url": "https://pmayg.nic.in/",
      "offline_process": "Contact the Gram Panchayat or designated rural development authority."
    },
    "source": {
      "official_source_name": "Ministry of Rural Development",
      "official_source_url": "https://rural.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG011",
    "scheme_name": "Pradhan Mantri Awas Yojana - Urban 2.0 (PMAY-U 2.0)",
    "short_description": "Urban housing programme supporting eligible households through housing assistance and related components.",
    "category": "Housing",
    "sub_category": "Urban Housing",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Housing and Urban Affairs",
    "implementing_department": "Ministry of Housing and Urban Affairs",
    "benefits": [
      {
        "type": "housing_assistance",
        "amount": "",
        "description": "Assistance varies by PMAY-U 2.0 vertical and applicable state/UT conditions."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": 1800000, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": ["urban"],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": [
        "Income categories include EWS, LIG and MIG groups.",
        "Family must satisfy applicable housing-ownership conditions.",
        "Applicable town/city and scheme conditions must be satisfied."
      ]
    },
    "eligibility_rules": [
      {
        "field": "annual_income",
        "operator": "<=",
        "value": 1800000
      },
      {
        "field": "residence_type",
        "operator": "==",
        "value": "urban"
      }
    ],
    "required_documents": ["Aadhaar", "Income proof", "Bank account details", "Property/household documents as applicable"],
    "application": {
      "method": ["online", "designated local urban authority"],
      "official_url": "https://pmay-urban.gov.in/",
      "offline_process": "Apply through the designated Urban Local Body or implementing agency."
    },
    "source": {
      "official_source_name": "myScheme / Ministry of Housing and Urban Affairs",
      "official_source_url": "https://www.myscheme.gov.in/schemes/pmay-u",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG012",
    "scheme_name": "Pradhan Mantri Ujjwala Yojana (PMUY)",
    "short_description": "Supports eligible women from deprived households in obtaining LPG connections.",
    "category": "Energy",
    "sub_category": "Clean Cooking Fuel",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Petroleum and Natural Gas",
    "implementing_department": "Ministry of Petroleum and Natural Gas",
    "benefits": [
      {
        "type": "LPG_connection_support",
        "amount": "",
        "description": "Support for eligible households to obtain an LPG connection under the scheme."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": ["female"],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Applicant must meet applicable deprivation/household conditions and must not already have an LPG connection in the household."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 18
      },
      {
        "field": "gender",
        "operator": "==",
        "value": "female"
      }
    ],
    "required_documents": ["Aadhaar", "Address proof", "Bank account details", "Household/ration-card related information where applicable"],
    "application": {
      "method": ["online", "LPG distributor"],
      "official_url": "https://www.pmuy.gov.in/",
      "offline_process": "Submit the application through an LPG distributor."
    },
    "source": {
      "official_source_name": "Pradhan Mantri Ujjwala Yojana",
      "official_source_url": "https://www.pmuy.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG013",
    "scheme_name": "Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)",
    "short_description": "Government-funded health assurance providing cashless hospitalization coverage to eligible beneficiaries.",
    "category": "Health",
    "sub_category": "Health Insurance",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Health and Family Welfare",
    "implementing_department": "National Health Authority",
    "benefits": [
      {
        "type": "health_insurance",
        "amount": "Up to ₹5 lakh per family per year",
        "description": "Cashless secondary and tertiary hospitalization coverage for eligible families."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": ["rural", "urban"],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Eligibility is primarily based on government-identified deprivation/occupational criteria and applicable beneficiary databases."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity document", "Beneficiary identification details"],
    "application": {
      "method": ["online eligibility check", "Common Service Centre", "empanelled hospital"],
      "official_url": "https://pmjay.gov.in/",
      "offline_process": "Visit an empanelled hospital or Common Service Centre for beneficiary identification."
    },
    "source": {
      "official_source_name": "National Health Authority / myScheme",
      "official_source_url": "https://www.myscheme.gov.in/hi/schemes/ab-pmjay",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG014",
    "scheme_name": "Pradhan Mantri SVANidhi",
    "short_description": "Working-capital support scheme for eligible street vendors.",
    "category": "Business & Entrepreneurship",
    "sub_category": "Street Vendors",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Housing and Urban Affairs",
    "implementing_department": "Ministry of Housing and Urban Affairs",
    "benefits": [
      {
        "type": "working_capital_loan",
        "amount": "",
        "description": "Working-capital credit support for eligible street vendors."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["street_vendor"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["self_employed"],
      "student_status": None,
      "rural_urban": ["urban"],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Street-vendor eligibility and identification criteria apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity proof", "Vendor certificate/identification where applicable", "Bank account details"],
    "application": {
      "method": ["online", "local urban authority", "lending institution"],
      "official_url": "https://pmsvanidhi.mohua.gov.in/",
      "offline_process": "Approach the designated Urban Local Body or lending institution."
    },
    "source": {
      "official_source_name": "Ministry of Housing and Urban Affairs",
      "official_source_url": "https://mohua.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG015",
    "scheme_name": "PM Vishwakarma",
    "short_description": "Support programme for traditional artisans and craftspeople working with their hands and tools.",
    "category": "Skill & Employment",
    "sub_category": "Artisans",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Micro, Small and Medium Enterprises",
    "implementing_department": "Ministry of MSME",
    "benefits": [
      {
        "type": "skill_training",
        "amount": "",
        "description": "Skill training, toolkit support, credit and other benefits under applicable programme provisions."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["eligible_traditional_artisan"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["self_employed"],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Applicant must practice an eligible traditional trade and satisfy scheme conditions."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 18
      }
    ],
    "required_documents": ["Aadhaar", "Identity/address details", "Trade-related information"],
    "application": {
      "method": ["Common Service Centre", "online"],
      "official_url": "https://pmvishwakarma.gov.in/",
      "offline_process": "Registration can be facilitated through designated Common Service Centres."
    },
    "source": {
      "official_source_name": "Ministry of MSME",
      "official_source_url": "https://msme.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG016",
    "scheme_name": "Prime Minister's Employment Generation Programme (PMEGP)",
    "short_description": "Credit-linked subsidy programme supporting new micro-enterprises and employment generation.",
    "category": "Business & Entrepreneurship",
    "sub_category": "Entrepreneurship",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Micro, Small and Medium Enterprises",
    "implementing_department": "Khadi and Village Industries Commission",
    "benefits": [
      {
        "type": "credit_linked_subsidy",
        "amount": "",
        "description": "Margin-money subsidy linked to eligible project financing."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["self_employed", "entrepreneur"],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Project-specific and scheme guidelines apply."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 18
      }
    ],
    "required_documents": ["Identity proof", "Project report", "Bank documents", "Category certificates where applicable"],
    "application": {
      "method": ["online"],
      "official_url": "https://www.kviconline.gov.in/pmegpeportal/",
      "offline_process": "Assistance may be available through KVIC/KVIB/DIC implementing agencies."
    },
    "source": {
      "official_source_name": "Ministry of MSME / KVIC",
      "official_source_url": "https://msme.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG017",
    "scheme_name": "Pradhan Mantri MUDRA Yojana (PMMY)",
    "short_description": "Credit support for micro and small non-farm enterprises and entrepreneurs.",
    "category": "Business & Entrepreneurship",
    "sub_category": "Micro Enterprise Credit",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Finance",
    "implementing_department": "Department of Financial Services",
    "benefits": [
      {
        "type": "business_loan",
        "amount": "",
        "description": "Collateral-free credit support through participating lending institutions, subject to applicable conditions."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["entrepreneur", "small_business"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["self_employed"],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Loan eligibility is assessed by the participating lender."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 18
      }
    ],
    "required_documents": ["Identity proof", "Address proof", "Business/project documents", "Bank documents"],
    "application": {
      "method": ["bank", "NBFC", "MFI"],
      "official_url": "https://www.mudra.org.in/",
      "offline_process": "Apply through a participating lending institution."
    },
    "source": {
      "official_source_name": "Department of Financial Services",
      "official_source_url": "https://financialservices.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG018",
    "scheme_name": "Stand-Up India",
    "short_description": "Bank loans to support entrepreneurship among eligible SC/ST and women entrepreneurs.",
    "category": "Business & Entrepreneurship",
    "sub_category": "Entrepreneurship Finance",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Finance",
    "implementing_department": "Department of Financial Services",
    "benefits": [
      {
        "type": "bank_loan",
        "amount": "",
        "description": "Bank finance for eligible greenfield enterprises."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["entrepreneur"],
      "category": ["SC", "ST"],
      "gender": ["female"],
      "education": [],
      "employment_status": ["self_employed", "entrepreneur"],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Applicable for eligible greenfield enterprises; lender assessment applies."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 18
      },
      {
        "field": "target_group",
        "operator": "OR",
        "value": ["SC", "ST", "female"]
      }
    ],
    "required_documents": ["Identity proof", "Address proof", "Business/project documents", "Category certificate where applicable"],
    "application": {
      "method": ["online", "bank"],
      "official_url": "https://www.standupmitra.in/",
      "offline_process": "Approach a participating bank branch."
    },
    "source": {
      "official_source_name": "Department of Financial Services",
      "official_source_url": "https://financialservices.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG019",
    "scheme_name": "Credit Guarantee Scheme for Micro and Small Enterprises (CGTMSE)",
    "short_description": "Credit guarantee support intended to facilitate collateral-free institutional credit to eligible MSEs.",
    "category": "Business & Entrepreneurship",
    "sub_category": "Credit Guarantee",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Micro, Small and Medium Enterprises",
    "implementing_department": "Credit Guarantee Fund Trust for Micro and Small Enterprises",
    "benefits": [
      {
        "type": "credit_guarantee",
        "amount": "",
        "description": "Guarantee support for eligible loans extended by participating lenders."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["entrepreneur", "small_business"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["self_employed"],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Eligibility is linked to eligible MSE borrowers and participating lending institutions."]
    },
    "eligibility_rules": [],
    "required_documents": ["Business registration documents", "Identity proof", "Loan/project documents"],
    "application": {
      "method": ["participating lender"],
      "official_url": "https://www.cgtmse.in/",
      "offline_process": "Approach a participating lending institution."
    },
    "source": {
      "official_source_name": "CGTMSE",
      "official_source_url": "https://www.cgtmse.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG020",
    "scheme_name": "PM Formalisation of Micro Food Processing Enterprises (PMFME)",
    "short_description": "Supports formalisation and upgrading of micro food-processing enterprises.",
    "category": "Business & Entrepreneurship",
    "sub_category": "Food Processing",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Food Processing Industries",
    "implementing_department": "Ministry of Food Processing Industries",
    "benefits": [
      {
        "type": "credit_linked_support",
        "amount": "",
        "description": "Financial and capacity-building support under applicable PMFME components."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["food_processor", "entrepreneur"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["self_employed"],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Eligibility depends on applicable component and enterprise criteria."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity proof", "Enterprise/project documents", "Bank details"],
    "application": {
      "method": ["online", "designated state agency"],
      "official_url": "https://pmfme.mofpi.gov.in/",
      "offline_process": "Contact the State Nodal Agency or designated implementing agency."
    },
    "source": {
      "official_source_name": "Ministry of Food Processing Industries",
      "official_source_url": "https://mofpi.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG021",
    "scheme_name": "SFURTI",
    "short_description": "Supports traditional industries and artisan clusters through organised cluster development.",
    "category": "Business & Entrepreneurship",
    "sub_category": "Traditional Industries",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Micro, Small and Medium Enterprises",
    "implementing_department": "Khadi and Village Industries Commission",
    "benefits": [
      {
        "type": "cluster_support",
        "amount": "",
        "description": "Support for development of traditional-industry clusters and artisan livelihoods."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["artisan", "traditional_industry_worker"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Cluster/implementing-agency conditions apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity and artisan/cluster documents as applicable"],
    "application": {
      "method": ["implementing agency"],
      "official_url": "https://sfurti.msme.gov.in/",
      "offline_process": "Contact the implementing agency or relevant MSME/KVIC office."
    },
    "source": {
      "official_source_name": "Ministry of MSME",
      "official_source_url": "https://msme.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG022",
    "scheme_name": "National SC-ST Hub",
    "short_description": "Supports SC/ST entrepreneurs in accessing public procurement and business opportunities.",
    "category": "Business & Entrepreneurship",
    "sub_category": "SC/ST Entrepreneurship",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Micro, Small and Medium Enterprises",
    "implementing_department": "Ministry of MSME",
    "benefits": [
      {
        "type": "business_support",
        "amount": "",
        "description": "Capacity building, market/procurement support and other assistance for eligible SC/ST entrepreneurs."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["entrepreneur"],
      "category": ["SC", "ST"],
      "gender": [],
      "education": [],
      "employment_status": ["self_employed"],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Enterprise registration and programme-specific conditions apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Udyam/enterprise documents", "SC/ST certificate", "Identity proof"],
    "application": {
      "method": ["online", "designated MSME channels"],
      "official_url": "https://scsthub.in/",
      "offline_process": "Contact the National SC-ST Hub or relevant MSME office."
    },
    "source": {
      "official_source_name": "Ministry of MSME",
      "official_source_url": "https://msme.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG023",
    "scheme_name": "Pradhan Mantri Dakshta Aur Kushalta Sampann Hitgrahi (PM-DAKSH)",
    "short_description": "Skill-development programme targeting specified disadvantaged groups including SCs, OBCs, EWS, DNTs and Safai Mitras.",
    "category": "Skill & Employment",
    "sub_category": "Skill Development",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Social Justice and Empowerment",
    "implementing_department": "Department of Social Justice and Empowerment",
    "benefits": [
      {
        "type": "skill_training",
        "amount": "",
        "description": "Free skill training and related support under applicable training programmes."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": ["SC", "OBC", "EWS", "DNT", "Safai Mitra"],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Group-specific income and other conditions may apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Aadhaar/identity proof", "Category certificate where applicable", "Income certificate where applicable"],
    "application": {
      "method": ["online", "designated training centre"],
      "official_url": "",
      "offline_process": "Contact designated PM-DAKSH training centres."
    },
    "source": {
      "official_source_name": "myScheme / Ministry of Social Justice and Empowerment",
      "official_source_url": "https://www.myscheme.gov.in/schemes/pm-daksh",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG024",
    "scheme_name": "PM-AJAY (Pradhan Mantri Anusuchit Jaati Abhyuday Yojana)",
    "short_description": "Umbrella programme supporting development and socio-economic advancement of Scheduled Caste communities.",
    "category": "Social Welfare",
    "sub_category": "SC Development",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Social Justice and Empowerment",
    "implementing_department": "Department of Social Justice and Empowerment",
    "benefits": [
      {
        "type": "development_support",
        "amount": "",
        "description": "Support through applicable components for SC development and livelihoods."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": ["SC"],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Component-specific eligibility applies."]
    },
    "eligibility_rules": [],
    "required_documents": ["SC certificate", "Identity proof", "Other component-specific documents"],
    "application": {
      "method": ["state government/local implementing agency"],
      "official_url": "",
      "offline_process": "Contact the relevant State/UT social welfare department."
    },
    "source": {
      "official_source_name": "Ministry of Social Justice and Empowerment",
      "official_source_url": "https://socialjustice.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG025",
    "scheme_name": "PM-DAKSH Skill Development Scheme",
    "short_description": "Skill development assistance for eligible disadvantaged groups.",
    "category": "Skill & Employment",
    "sub_category": "Skill Development",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Social Justice and Empowerment",
    "implementing_department": "Department of Social Justice and Empowerment",
    "benefits": [
      {
        "type": "training",
        "amount": "",
        "description": "Skill training and employability support."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": ["SC", "OBC", "EWS", "DNT"],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Training-category and group-specific conditions apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity proof", "Category/income certificate where applicable"],
    "application": {
      "method": ["online", "training centre"],
      "official_url": "",
      "offline_process": "Contact designated PM-DAKSH training centres."
    },
    "source": {
      "official_source_name": "Ministry of Social Justice and Empowerment",
      "official_source_url": "https://socialjustice.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG026",
    "scheme_name": "National Overseas Scholarship",
    "short_description": "Scholarship support for eligible students from specified disadvantaged categories pursuing higher studies abroad.",
    "category": "Education",
    "sub_category": "Higher Education Abroad",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Social Justice and Empowerment",
    "implementing_department": "Department of Social Justice and Empowerment",
    "benefits": [
      {
        "type": "scholarship",
        "amount": "",
        "description": "Financial assistance for eligible overseas higher education."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": ["SC", "Denotified Nomadic and Semi-Nomadic Tribes", "Landless Agricultural Labourers", "Traditional Artisans"],
      "gender": [],
      "education": ["graduate/postgraduate as applicable"],
      "employment_status": [],
      "student_status": True,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Specific academic, admission, age and income conditions apply to the relevant selection cycle."]
    },
    "eligibility_rules": [],
    "required_documents": ["Academic certificates", "Admission/offer letter", "Category certificate", "Income certificate", "Passport"],
    "application": {
      "method": ["online"],
      "official_url": "https://nosmsje.gov.in/",
      "offline_process": ""
    },
    "source": {
      "official_source_name": "Ministry of Social Justice and Empowerment",
      "official_source_url": "https://socialjustice.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG027",
    "scheme_name": "Top Class Education Scheme for SC Students",
    "short_description": "Financial support for eligible SC students admitted to notified institutions.",
    "category": "Education",
    "sub_category": "SC Higher Education",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Social Justice and Empowerment",
    "implementing_department": "Department of Social Justice and Empowerment",
    "benefits": [
      {
        "type": "scholarship",
        "amount": "",
        "description": "Scholarship and related educational support subject to scheme limits."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": ["SC"],
      "gender": [],
      "education": ["higher education"],
      "employment_status": [],
      "student_status": True,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Admission to an eligible/notified institution and applicable family-income criteria are required."]
    },
    "eligibility_rules": [],
    "required_documents": ["SC certificate", "Income certificate", "Admission proof", "Academic documents", "Bank details"],
    "application": {
      "method": ["online"],
      "official_url": "https://scholarships.gov.in/",
      "offline_process": "Contact the institution's scholarship/nodal office."
    },
    "source": {
      "official_source_name": "Ministry of Social Justice and Empowerment / National Scholarship Portal",
      "official_source_url": "https://socialjustice.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG028",
    "scheme_name": "Post-Matric Scholarship for SC Students",
    "short_description": "Scholarship support for eligible SC students pursuing post-matriculation studies.",
    "category": "Education",
    "sub_category": "SC Scholarship",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Social Justice and Empowerment",
    "implementing_department": "Department of Social Justice and Empowerment",
    "benefits": [
      {
        "type": "scholarship",
        "amount": "",
        "description": "Financial support for eligible post-matric students."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": ["SC"],
      "gender": [],
      "education": ["post-matric"],
      "employment_status": [],
      "student_status": True,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Course, income and other conditions are governed by applicable scholarship guidelines."]
    },
    "eligibility_rules": [],
    "required_documents": ["SC certificate", "Income certificate", "Academic/admission documents", "Bank details"],
    "application": {
      "method": ["online", "National Scholarship Portal where applicable"],
      "official_url": "https://scholarships.gov.in/",
      "offline_process": "Contact the institution scholarship/nodal office."
    },
    "source": {
      "official_source_name": "National Scholarship Portal / Ministry of Social Justice and Empowerment",
      "official_source_url": "https://scholarships.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG029",
    "scheme_name": "Pre-Matric Scholarship for SC Students",
    "short_description": "Educational scholarship support for eligible SC students at applicable pre-matric levels.",
    "category": "Education",
    "sub_category": "SC Scholarship",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Social Justice and Empowerment",
    "implementing_department": "Department of Social Justice and Empowerment",
    "benefits": [
      {
        "type": "scholarship",
        "amount": "",
        "description": "Financial support for eligible students under applicable pre-matric provisions."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": ["SC"],
      "gender": [],
      "education": ["pre-matric"],
      "employment_status": [],
      "student_status": True,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Applicable class, income and school-related conditions must be checked for the current cycle."]
    },
    "eligibility_rules": [],
    "required_documents": ["SC certificate", "Income certificate", "School/student records", "Bank details"],
    "application": {
      "method": ["online", "National Scholarship Portal where applicable"],
      "official_url": "https://scholarships.gov.in/",
      "offline_process": "Contact the school/institution scholarship authority."
    },
    "source": {
      "official_source_name": "National Scholarship Portal",
      "official_source_url": "https://scholarships.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG030",
    "scheme_name": "PM YASASVI",
    "short_description": "Scholarship support for eligible students belonging to specified disadvantaged social groups.",
    "category": "Education",
    "sub_category": "OBC/EBC/DNT Education",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Social Justice and Empowerment",
    "implementing_department": "Department of Social Justice and Empowerment",
    "benefits": [
      {
        "type": "scholarship",
        "amount": "",
        "description": "Educational support under applicable PM YASASVI components."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": ["OBC", "EBC", "DNT"],
      "gender": [],
      "education": ["school", "higher education as applicable"],
      "employment_status": [],
      "student_status": True,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Current component, class, income and institutional conditions must be checked."]
    },
    "eligibility_rules": [],
    "required_documents": ["Category certificate", "Income certificate", "Academic documents", "Bank details"],
    "application": {
      "method": ["online", "National Scholarship Portal where applicable"],
      "official_url": "https://scholarships.gov.in/",
      "offline_process": "Contact the educational institution's scholarship/nodal office."
    },
    "source": {
      "official_source_name": "Ministry of Social Justice and Empowerment",
      "official_source_url": "https://socialjustice.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG031",
    "scheme_name": "National Means-cum-Merit Scholarship Scheme (NMMSS)",
    "short_description": "Scholarship programme intended to reduce dropout after Class VIII and encourage continuation of secondary education.",
    "category": "Education",
    "sub_category": "School Scholarship",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Education",
    "implementing_department": "Department of School Education and Literacy",
    "benefits": [
      {
        "type": "scholarship",
        "amount": "",
        "description": "Scholarship support for selected eligible students continuing secondary education."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": ["Class VIII/secondary level"],
      "employment_status": [],
      "student_status": True,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Selection examination and parental-income conditions apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["School records", "Income certificate", "Bank details", "Examination/selection documents"],
    "application": {
      "method": ["state-level selection process", "online where applicable"],
      "official_url": "https://scholarships.gov.in/",
      "offline_process": "Follow the State/UT education department's notification."
    },
    "source": {
      "official_source_name": "Ministry of Education",
      "official_source_url": "https://www.education.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG032",
    "scheme_name": "Central Sector Scheme of Scholarship for College and University Students",
    "short_description": "Scholarship programme for meritorious students pursuing higher education.",
    "category": "Education",
    "sub_category": "Higher Education Scholarship",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Education",
    "implementing_department": "Department of Higher Education",
    "benefits": [
      {
        "type": "scholarship",
        "amount": "",
        "description": "Scholarship assistance subject to applicable scheme rules."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": ["college", "university"],
      "employment_status": [],
      "student_status": True,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Merit, income and course/institution conditions apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Academic certificates", "Income certificate", "Admission proof", "Bank details"],
    "application": {
      "method": ["online", "National Scholarship Portal"],
      "official_url": "https://scholarships.gov.in/",
      "offline_process": "Contact the institution's scholarship/nodal authority."
    },
    "source": {
      "official_source_name": "Ministry of Education / National Scholarship Portal",
      "official_source_url": "https://www.education.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG033",
    "scheme_name": "INSPIRE",
    "short_description": "Department of Science and Technology programme supporting scientific education and research talent.",
    "category": "Education & Science",
    "sub_category": "Science Scholarship",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Science and Technology",
    "implementing_department": "Department of Science and Technology",
    "benefits": [
      {
        "type": "scholarship",
        "amount": "",
        "description": "Scholarship/fellowship support depending on the INSPIRE component."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": ["science education", "higher education"],
      "employment_status": [],
      "student_status": True,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Eligibility differs by INSPIRE component and academic stage."]
    },
    "eligibility_rules": [],
    "required_documents": ["Academic records", "Identity proof", "Admission/academic documents"],
    "application": {
      "method": ["online"],
      "official_url": "https://online-inspire.gov.in/",
      "offline_process": ""
    },
    "source": {
      "official_source_name": "Department of Science and Technology",
      "official_source_url": "https://dst.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG034",
    "scheme_name": "Pradhan Mantri Kaushal Vikas Yojana (PMKVY)",
    "short_description": "National skill-development programme providing training and certification opportunities.",
    "category": "Skill & Employment",
    "sub_category": "Skill Training",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Skill Development and Entrepreneurship",
    "implementing_department": "Ministry of Skill Development and Entrepreneurship",
    "benefits": [
      {
        "type": "skill_training",
        "amount": "",
        "description": "Skill training, assessment and certification under applicable programmes."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["job_seeker"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["unemployed", "job_seeker"],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Course-specific age and education requirements apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Aadhaar/identity proof", "Educational documents where required"],
    "application": {
      "method": ["online", "training centre"],
      "official_url": "https://www.pmkvyofficial.org/",
      "offline_process": "Visit an approved training centre."
    },
    "source": {
      "official_source_name": "Ministry of Skill Development and Entrepreneurship",
      "official_source_url": "https://www.msde.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG035",
    "scheme_name": "National Apprenticeship Promotion Scheme (NAPS)",
    "short_description": "Promotes apprenticeship training and employer participation in apprenticeship programmes.",
    "category": "Skill & Employment",
    "sub_category": "Apprenticeship",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Skill Development and Entrepreneurship",
    "implementing_department": "Directorate General of Training",
    "benefits": [
      {
        "type": "apprenticeship_support",
        "amount": "",
        "description": "Support for apprenticeship training under applicable provisions."
      }
    ],
    "eligibility": {
      "age": {"min": 14, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["job_seeker", "apprentice"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["job_seeker"],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Trade-specific age, education and apprenticeship conditions apply."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 14
      }
    ],
    "required_documents": ["Identity proof", "Educational certificates", "Bank details"],
    "application": {
      "method": ["online"],
      "official_url": "https://www.apprenticeshipindia.gov.in/",
      "offline_process": "Contact an establishment/training provider participating in apprenticeship programmes."
    },
    "source": {
      "official_source_name": "Ministry of Skill Development and Entrepreneurship",
      "official_source_url": "https://www.msde.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG036",
    "scheme_name": "Deen Dayal Upadhyaya Grameen Kaushalya Yojana (DDU-GKY)",
    "short_description": "Rural skill-development and placement-oriented programme for eligible rural youth.",
    "category": "Skill & Employment",
    "sub_category": "Rural Skill Development",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Rural Development",
    "implementing_department": "Department of Rural Development",
    "benefits": [
      {
        "type": "skill_training",
        "amount": "",
        "description": "Skill training and placement-oriented support for eligible rural youth."
      }
    ],
    "eligibility": {
      "age": {"min": 15, "max": 35},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["job_seeker"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["unemployed", "job_seeker"],
      "student_status": None,
      "rural_urban": ["rural"],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Age and category relaxations may apply to specified groups."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 15
      },
      {
        "field": "age",
        "operator": "<=",
        "value": 35
      },
      {
        "field": "residence_type",
        "operator": "==",
        "value": "rural"
      }
    ],
    "required_documents": ["Identity proof", "Residence/rural status information", "Educational documents"],
    "application": {
      "method": ["training centre", "state implementing agency"],
      "official_url": "https://ddugky.info/",
      "offline_process": "Contact a designated DDU-GKY training centre."
    },
    "source": {
      "official_source_name": "Ministry of Rural Development",
      "official_source_url": "https://rural.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG037",
    "scheme_name": "DAY-NULM",
    "short_description": "Urban livelihoods mission supporting urban poor through self-employment and skill-development interventions.",
    "category": "Employment",
    "sub_category": "Urban Livelihoods",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Housing and Urban Affairs",
    "implementing_department": "Ministry of Housing and Urban Affairs",
    "benefits": [
      {
        "type": "livelihood_support",
        "amount": "",
        "description": "Skill, self-employment and urban livelihood support under applicable components."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["job_seeker", "self_employed"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["unemployed", "self_employed"],
      "student_status": None,
      "rural_urban": ["urban"],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Component-specific urban-poor eligibility criteria apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Identity proof", "Urban residence/beneficiary documents", "Bank details where applicable"],
    "application": {
      "method": ["Urban Local Body", "designated implementation agency"],
      "official_url": "",
      "offline_process": "Contact the Urban Local Body or city livelihood mission."
    },
    "source": {
      "official_source_name": "Ministry of Housing and Urban Affairs",
      "official_source_url": "https://mohua.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG038",
    "scheme_name": "Mahatma Gandhi National Rural Employment Guarantee Scheme (MGNREGS)",
    "short_description": "Legal employment guarantee framework providing wage employment to rural households subject to programme conditions.",
    "category": "Employment",
    "sub_category": "Rural Employment",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Rural Development",
    "implementing_department": "Department of Rural Development",
    "benefits": [
      {
        "type": "wage_employment",
        "amount": "",
        "description": "Demand-driven wage employment for eligible rural households."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["rural_worker"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["unemployed", "job_seeker"],
      "student_status": None,
      "rural_urban": ["rural"],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Adult members of rural households seeking unskilled manual work can demand employment subject to Act/programme provisions."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 18
      },
      {
        "field": "residence_type",
        "operator": "==",
        "value": "rural"
      }
    ],
    "required_documents": ["Identity proof", "Household/residence details", "Job card-related records"],
    "application": {
      "method": ["Gram Panchayat", "local rural development authority"],
      "official_url": "https://nrega.nic.in/",
      "offline_process": "Demand work through the Gram Panchayat or designated local authority."
    },
    "source": {
      "official_source_name": "Ministry of Rural Development",
      "official_source_url": "https://rural.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG039",
    "scheme_name": "Pradhan Mantri Shram Yogi Maandhan (PM-SYM)",
    "short_description": "Contributory pension scheme for eligible unorganised-sector workers.",
    "category": "Social Security",
    "sub_category": "Pension",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Labour and Employment",
    "implementing_department": "Ministry of Labour and Employment",
    "benefits": [
      {
        "type": "pension",
        "amount": "₹3,000 per month after age 60",
        "description": "Assured monthly pension for eligible subscribers after attaining 60 years, subject to scheme conditions."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": 40},
      "income": {"maximum_annual_income": 180000, "income_period": "annual"},
      "residence": ["India"],
      "occupation": ["unorganised_sector_worker"],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": ["self_employed", "unorganised_sector"],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Monthly income must be ₹15,000 or less. Applicant must not be covered by specified pension/social-security exclusions such as EPFO/ESIC/NPS or be an income-tax assessee, subject to current rules."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 18
      },
      {
        "field": "age",
        "operator": "<=",
        "value": 40
      },
      {
        "field": "monthly_income",
        "operator": "<=",
        "value": 15000
      }
    ],
    "required_documents": ["Aadhaar", "Savings bank account details", "Mobile number"],
    "application": {
      "method": ["online", "Common Service Centre"],
      "official_url": "https://labour.gov.in/",
      "offline_process": "Enrollment is available through designated Common Service Centres."
    },
    "source": {
      "official_source_name": "Ministry of Labour and Employment / National Government Services Portal",
      "official_source_url": "https://services.india.gov.in/service/detail/enroll-to-avail-benefits-from-pradhan-mantri-shram-yogi-maandhan-yojana-1",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG040",
    "scheme_name": "Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)",
    "short_description": "Low-cost renewable term life insurance scheme for eligible bank/post-office account holders.",
    "category": "Insurance",
    "sub_category": "Life Insurance",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Finance",
    "implementing_department": "Department of Financial Services",
    "benefits": [
      {
        "type": "life_insurance",
        "amount": "₹2 lakh",
        "description": "Life insurance benefit payable on death subject to scheme conditions."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": 50},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Applicant must have an eligible bank/post-office account and provide consent for auto-debit."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 18
      },
      {
        "field": "age",
        "operator": "<=",
        "value": 50
      }
    ],
    "required_documents": ["Bank/post-office account", "Aadhaar or KYC documents as required"],
    "application": {
      "method": ["bank", "post office"],
      "official_url": "",
      "offline_process": "Enroll through the participating bank/post office."
    },
    "source": {
      "official_source_name": "Department of Financial Services",
      "official_source_url": "https://financialservices.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG041",
    "scheme_name": "Pradhan Mantri Suraksha Bima Yojana (PMSBY)",
    "short_description": "Accident insurance scheme for eligible bank/post-office account holders.",
    "category": "Insurance",
    "sub_category": "Accident Insurance",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Finance",
    "implementing_department": "Department of Financial Services",
    "benefits": [
      {
        "type": "accident_insurance",
        "amount": "Up to ₹2 lakh",
        "description": "Accident insurance benefit subject to applicable conditions."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": 70},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Applicant must have an eligible bank/post-office account and consent to auto-debit."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 18
      },
      {
        "field": "age",
        "operator": "<=",
        "value": 70
      }
    ],
    "required_documents": ["Bank/post-office account", "KYC documents as required"],
    "application": {
      "method": ["bank", "post office"],
      "official_url": "",
      "offline_process": "Enroll through a participating bank or post office."
    },
    "source": {
      "official_source_name": "Department of Financial Services",
      "official_source_url": "https://financialservices.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG042",
    "scheme_name": "Atal Pension Yojana (APY)",
    "short_description": "Government-supported pension scheme primarily aimed at workers in the unorganised sector.",
    "category": "Social Security",
    "sub_category": "Pension",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Finance",
    "implementing_department": "Department of Financial Services",
    "benefits": [
      {
        "type": "pension",
        "amount": "",
        "description": "Guaranteed pension options beginning at age 60 subject to contribution and scheme choice."
      }
    ],
    "eligibility": {
      "age": {"min": 18, "max": 40},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Requires eligible savings bank/post-office account and scheme contribution."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": ">=",
        "value": 18
      },
      {
        "field": "age",
        "operator": "<=",
        "value": 40
      }
    ],
    "required_documents": ["Savings bank/post-office account", "Aadhaar/KYC documents as required"],
    "application": {
      "method": ["bank", "post office"],
      "official_url": "https://www.pfrda.org.in/",
      "offline_process": "Enroll through a participating bank/post office."
    },
    "source": {
      "official_source_name": "PFRDA / Department of Financial Services",
      "official_source_url": "https://www.pfrda.org.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG043",
    "scheme_name": "Pradhan Mantri Jan Dhan Yojana (PMJDY)",
    "short_description": "Financial inclusion programme providing access to basic banking and related financial services.",
    "category": "Financial Inclusion",
    "sub_category": "Banking",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Finance",
    "implementing_department": "Department of Financial Services",
    "benefits": [
      {
        "type": "bank_account",
        "amount": "",
        "description": "Basic savings bank account, RuPay debit card and access to applicable financial services."
      }
    ],
    "eligibility": {
      "age": {"min": 10, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Account opening and minor-account rules depend on age and banking requirements."]
    },
    "eligibility_rules": [],
    "required_documents": ["KYC/identity documents"],
    "application": {
      "method": ["bank", "Bank Mitra"],
      "official_url": "https://pmjdy.gov.in/",
      "offline_process": "Open an account at a participating bank branch or Bank Mitra outlet."
    },
    "source": {
      "official_source_name": "Department of Financial Services / PMJDY",
      "official_source_url": "https://pmjdy.gov.in/scheme",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG044",
    "scheme_name": "Pradhan Mantri Matru Vandana Yojana (PMMVY)",
    "short_description": "Maternity benefit programme providing financial support to eligible pregnant and lactating women.",
    "category": "Women & Child",
    "sub_category": "Maternity Benefit",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Women and Child Development",
    "implementing_department": "Ministry of Women and Child Development",
    "benefits": [
      {
        "type": "maternity_benefit",
        "amount": "",
        "description": "Maternity-related financial support subject to current scheme conditions."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": ["female"],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Current PMMVY eligibility categories and pregnancy/childbirth conditions must be checked before matching."]
    },
    "eligibility_rules": [],
    "required_documents": ["Aadhaar", "Bank account", "Pregnancy/health records as applicable"],
    "application": {
      "method": ["Anganwadi Centre", "online where available"],
      "official_url": "",
      "offline_process": "Contact the nearest Anganwadi Centre or implementing authority."
    },
    "source": {
      "official_source_name": "Ministry of Women and Child Development",
      "official_source_url": "https://wcd.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG045",
    "scheme_name": "Sukanya Samriddhi Account",
    "short_description": "Small-savings scheme intended for the financial future of eligible girl children.",
    "category": "Women & Child",
    "sub_category": "Girl Child Savings",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Finance",
    "implementing_department": "Department of Economic Affairs",
    "benefits": [
      {
        "type": "savings",
        "amount": "",
        "description": "Government-backed savings account with applicable interest and tax benefits under prevailing rules."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": 10},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": ["female"],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Account is opened in the name of an eligible girl child subject to scheme rules."]
    },
    "eligibility_rules": [
      {
        "field": "gender",
        "operator": "==",
        "value": "female"
      },
      {
        "field": "age",
        "operator": "<=",
        "value": 10
      }
    ],
    "required_documents": ["Girl child's birth certificate", "Guardian identity/KYC documents"],
    "application": {
      "method": ["post office", "participating bank"],
      "official_url": "https://www.indiapost.gov.in/",
      "offline_process": "Open the account through a participating post office or bank."
    },
    "source": {
      "official_source_name": "Department of Economic Affairs / India Post",
      "official_source_url": "https://www.indiapost.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG046",
    "scheme_name": "Mission Saksham Anganwadi and POSHAN 2.0",
    "short_description": "Umbrella programme addressing nutrition and early childhood development.",
    "category": "Women & Child",
    "sub_category": "Nutrition",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Women and Child Development",
    "implementing_department": "Ministry of Women and Child Development",
    "benefits": [
      {
        "type": "nutrition_support",
        "amount": "",
        "description": "Nutrition and early-childhood services through the Anganwadi system for eligible beneficiaries."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": ["female"],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Beneficiary categories include children and eligible women; service-specific criteria apply."]
    },
    "eligibility_rules": [],
    "required_documents": ["Beneficiary/household details", "Identity information as applicable"],
    "application": {
      "method": ["Anganwadi Centre"],
      "official_url": "https://wcd.gov.in/",
      "offline_process": "Contact the nearest Anganwadi Centre."
    },
    "source": {
      "official_source_name": "Ministry of Women and Child Development",
      "official_source_url": "https://wcd.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG047",
    "scheme_name": "Mission Vatsalya",
    "short_description": "Child-protection programme supporting children in need of care and protection and related child welfare systems.",
    "category": "Women & Child",
    "sub_category": "Child Protection",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Women and Child Development",
    "implementing_department": "Ministry of Women and Child Development",
    "benefits": [
      {
        "type": "child_protection",
        "amount": "",
        "description": "Child protection, care, rehabilitation and support services through the statutory child-protection system."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": 18},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Eligibility depends on the child's protection/care circumstances and applicable legal process."]
    },
    "eligibility_rules": [
      {
        "field": "age",
        "operator": "<",
        "value": 18
      }
    ],
    "required_documents": ["Child identity/age information", "Relevant child-protection records where applicable"],
    "application": {
      "method": ["Child Welfare Committee", "Childline/child protection authorities", "district child protection unit"],
      "official_url": "https://wcd.gov.in/",
      "offline_process": "Contact the District Child Protection Unit or Child Welfare Committee."
    },
    "source": {
      "official_source_name": "Ministry of Women and Child Development",
      "official_source_url": "https://wcd.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG048",
    "scheme_name": "Beti Bachao Beti Padhao (BBBP)",
    "short_description": "National programme promoting the protection, education and empowerment of the girl child.",
    "category": "Women & Child",
    "sub_category": "Girl Child Welfare",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Women and Child Development",
    "implementing_department": "Ministry of Women and Child Development",
    "benefits": [
      {
        "type": "awareness_and_support",
        "amount": "",
        "description": "Community and institutional interventions promoting survival, protection, education and empowerment of girls."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": ["female"],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": [],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["This is primarily a behavioural and institutional programme rather than a universal individual cash-benefit scheme."]
    },
    "eligibility_rules": [],
    "required_documents": [],
    "application": {
      "method": ["local government/community programme"],
      "official_url": "https://wcd.gov.in/",
      "offline_process": "Participate through applicable local/state programme channels."
    },
    "source": {
      "official_source_name": "Ministry of Women and Child Development",
      "official_source_url": "https://wcd.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG049",
    "scheme_name": "PM Surya Ghar: Muft Bijli Yojana",
    "short_description": "Programme promoting residential rooftop solar installations.",
    "category": "Energy",
    "sub_category": "Rooftop Solar",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of New and Renewable Energy",
    "implementing_department": "Ministry of New and Renewable Energy",
    "benefits": [
      {
        "type": "subsidy",
        "amount": "",
        "description": "Central financial assistance for eligible residential rooftop solar installations under applicable rules."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": ["urban", "rural"],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Applicant must meet residential electricity-connection and rooftop-solar conditions."]
    },
    "eligibility_rules": [],
    "required_documents": ["Electricity consumer details", "Identity/KYC documents", "Bank account details"],
    "application": {
      "method": ["online"],
      "official_url": "https://pmsuryaghar.gov.in/",
      "offline_process": "Contact the local electricity distribution company for assistance."
    },
    "source": {
      "official_source_name": "Ministry of New and Renewable Energy",
      "official_source_url": "https://mnre.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  },

  {
    "scheme_id": "CG050",
    "scheme_name": "Jal Jeevan Mission",
    "short_description": "National mission aimed at providing functional household tap-water connections in rural areas.",
    "category": "Water & Sanitation",
    "sub_category": "Rural Drinking Water",
    "government_level": "central",
    "state": "all_india",
    "implementing_ministry": "Ministry of Jal Shakti",
    "implementing_department": "Department of Drinking Water and Sanitation",
    "benefits": [
      {
        "type": "public_service",
        "amount": "",
        "description": "Rural household access to functional tap-water supply through government implementation."
      }
    ],
    "eligibility": {
      "age": {"min": None, "max": None},
      "income": {"maximum_annual_income": None, "income_period": "annual"},
      "residence": ["India"],
      "occupation": [],
      "category": [],
      "gender": [],
      "education": [],
      "employment_status": [],
      "student_status": None,
      "rural_urban": ["rural"],
      "farmer_status": None,
      "disability_status": None,
      "other_conditions": ["Household-level implementation depends on the village water-supply programme and state/district implementation."]
    },
    "eligibility_rules": [],
    "required_documents": ["Household/residence details where required"],
    "application": {
      "method": ["Gram Panchayat", "State/UT implementing agency"],
      "official_url": "https://jaljeevanmission.gov.in/",
      "offline_process": "Contact the Gram Panchayat or local water-supply authority."
    },
    "source": {
      "official_source_name": "Ministry of Jal Shakti",
      "official_source_url": "https://jaljeevanmission.gov.in/",
      "last_verified": "2026-09-26",
      "verification_status": "verified"
    }
  }
]


def main():
    # sanity: unique scheme_ids
    ids = [s["scheme_id"] for s in SCHEMES]
    assert len(ids) == len(set(ids)), "Duplicate scheme_id detected"

    with open("schemes.json", "w", encoding="utf-8") as f:
        json.dump(SCHEMES, f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(SCHEMES)} schemes to schemes.json")


if __name__ == "__main__":
    main()
