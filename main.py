import json
import os
import sys

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Load .env file automatically in the background (hidden from the user)
try:
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ.setdefault(
                    key.strip(), val.strip().strip('"').strip("'"))
except Exception:
    pass

# Import requests library
try:
    import requests
except ImportError:
    print("[System Error] The 'requests' library is required. Install it using: pip install requests")
    sys.exit(1)


# ==========================================================
# 1. READ & VALIDATE USER INPUT (Using try and except)
# ==========================================================
def get_user_input():
    print("\n" + "=" * 50)
    print("      ENTER USER DETAILS FOR SCHEME MATCHING")
    print("=" * 50)

    try:
        # Age
        age = int(input("1. Age: ").strip())
        if age <= 0 or age > 120:
            raise ValueError("Age must be between 1 and 120.")

        # Gender
        gender = input("2. Gender (female/male/other): ").strip().lower()
        if gender not in ["female", "male", "other"]:
            raise ValueError("Gender must be 'female', 'male', or 'other'.")

        # State
        state = input(
            "3. State (e.g. Maharashtra, Telangana, Uttar Pradesh): ").strip()
        if not state:
            raise ValueError("State cannot be empty.")

        # Residence
        residence = input("4. Residence (rural/urban): ").strip().lower()
        if residence not in ["rural", "urban"]:
            raise ValueError("Residence must be 'rural' or 'urban'.")

        # Occupation
        occupation = input(
            "5. Occupation (e.g. student, farmer, artisan, entrepreneur, unemployed): ").strip().lower()
        if not occupation:
            raise ValueError("Occupation cannot be empty.")

        # Education
        education = input(
            "6. Education (e.g. school, 10th, 12th, graduate, higher education): ").strip().lower()
        if not education:
            raise ValueError("Education cannot be empty.")

        # Category
        category = input(
            "7. Category (General/SC/ST/OBC/EWS): ").strip().upper()
        if category not in ["GENERAL", "SC", "ST", "OBC", "EWS"]:
            raise ValueError("Category must be General, SC, ST, OBC, or EWS.")

        # Annual Income
        annual_income = float(
            input("8. Annual Household Income (INR): ").strip())
        if annual_income < 0:
            raise ValueError("Annual income cannot be negative.")

        return {
            "age": age,
            "gender": gender,
            "state": state,
            "residence": residence,
            "occupation": occupation,
            "education": education,
            "category": category,
            "annual_income": annual_income,
            "is_farmer": "farmer" in occupation,
            "is_student": "student" in occupation or "student" in education
        }

    except ValueError as e:
        print(f"\n[Validation Error] {e}")
        return None
    except Exception as e:
        print(f"\n[Input Error] Failed to read input: {e}")
        return None


# ==========================================================
# 2. LOAD SCHEMES DATABASE (Using try and except)
# ==========================================================
def load_schemes(filepath="schemes.json"):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, filepath) if not os.path.isabs(
            filepath) else filepath

        with open(full_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"\n[Error] Database file '{filepath}' was not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"\n[Error] Invalid JSON format in '{filepath}': {e}")
        return None
    except Exception as e:
        print(f"\n[Error] Failed to load schemes database: {e}")
        return None


# ==========================================================
# 3. BASIC MATCHING (Deterministic Rule Filter)
# ==========================================================
def match_scheme(user, scheme):
    try:
        eligibility = scheme.get("eligibility", {})
        rules = scheme.get("eligibility_rules", [])

        # 1. Age check
        min_age = eligibility.get("age", {}).get("min")
        max_age = eligibility.get("age", {}).get("max")
        if min_age is not None and user["age"] < min_age:
            return False
        if max_age is not None and user["age"] > max_age:
            return False

        # 2. Income check
        max_income = eligibility.get("income", {}).get("maximum_annual_income")
        if max_income is not None and user["annual_income"] > max_income:
            return False

        # Check monthly income rule if present (e.g. PM-SYM <= 15000/month)
        for rule in rules:
            if rule.get("field") == "monthly_income" and rule.get("operator") == "<=":
                if (user["annual_income"] / 12) > rule.get("value"):
                    return False

        # 3. State check
        scheme_state = scheme.get("state", "all_india").lower()
        if scheme_state != "all_india" and scheme_state != user["state"].lower():
            return False

        # 4. Residence check (rural / urban)
        allowed_residence = [r.lower()
                             for r in eligibility.get("rural_urban", [])]
        if allowed_residence and user["residence"] not in allowed_residence:
            return False

        # 5. Gender & Social Category check (handles target_group OR rules like Stand-Up India)
        has_target_or_rule = False
        for rule in rules:
            if rule.get("field") == "target_group" and rule.get("operator") == "OR":
                has_target_or_rule = True
                allowed_targets = [t.lower() for t in rule.get("value", [])]
                if (user["gender"] not in allowed_targets) and (user["category"].lower() not in allowed_targets):
                    return False

        if not has_target_or_rule:
            allowed_genders = [g.lower()
                               for g in eligibility.get("gender", [])]
            if allowed_genders and user["gender"] not in allowed_genders:
                return False

            allowed_categories = [c.lower()
                                  for c in eligibility.get("category", [])]
            if allowed_categories:
                user_cat = user["category"].lower()
                if not any(user_cat == c or user_cat in c for c in allowed_categories):
                    return False

        # 6. Farmer check
        if eligibility.get("farmer_status") is True and not user["is_farmer"]:
            return False

        # 7. Student check
        if eligibility.get("student_status") is True and not user["is_student"]:
            return False

        # 8. Occupation and Employment Status check
        allowed_occupations = [o.lower()
                               for o in eligibility.get("occupation", [])]
        if allowed_occupations:
            user_occ = user["occupation"].lower()
            if not any(user_occ in o or o in user_occ for o in allowed_occupations):
                return False

        allowed_emp = [emp.lower()
                       for emp in eligibility.get("employment_status", [])]
        if allowed_emp:
            user_occ = user["occupation"].lower()
            if "student" in user_occ and not any(emp in ["job_seeker", "student", "unemployed"] for emp in allowed_emp):
                if not eligibility.get("student_status"):
                    return False

        # 9. Education check (filter out school-only/pre-matric schemes for adult students)
        scheme_education = [e.lower()
                            for e in eligibility.get("education", [])]
        if scheme_education:
            is_school_only = any(
                "pre-matric" in e or "class viii" in e for e in scheme_education)
            is_higher_ed = any(
                "higher" in e or "post-matric" in e or "college" in e or "university" in e or "graduate" in e for e in scheme_education)

            user_edu = user["education"].lower()
            user_is_adult = user["age"] >= 18

            if is_school_only and not is_higher_ed:
                if user_is_adult or any(h in user_edu for h in ["graduate", "college", "university", "higher", "post-matric", "12th"]):
                    return False

        return True

    except Exception as e:
        print(
            f"[Warning] Error matching scheme {scheme.get('scheme_id')}: {e}")
        return False


def get_official_url(scheme):
    """Extracts official website from application or source."""
    app_url = scheme.get("application", {}).get("official_url", "").strip()
    if app_url:
        return app_url
    return scheme.get("source", {}).get("official_source_url", "").strip()


# ==========================================================
# 4. OPENROUTER LLM API (Using try and except)
# ==========================================================
def call_openrouter_llm(user_profile, candidate_schemes, api_key):
    try:
        schemes_data = []
        for s in candidate_schemes:
            schemes_data.append({
                "scheme_id": s["scheme_id"],
                "scheme_name": s["scheme_name"],
                "short_description": s["short_description"],
                "benefits": s.get("benefits", []),
                "other_conditions": s.get("eligibility", {}).get("other_conditions", [])
            })

        prompt = f"""
You are an expert Indian Government welfare scheme eligibility analyst.
Analyze the user profile and candidate schemes that already passed preliminary filtering.

USER PROFILE:
{json.dumps(user_profile, indent=2)}

CANDIDATE SCHEMES:
{json.dumps(schemes_data, indent=2)}

PRACTICAL CLASSIFICATION RULES:
1. FULLY_MATCHED:
   - Mark as FULLY_MATCHED when the user profile directly satisfies all core requirements of the scheme (e.g. matching category, student/farmer status, education level, and income limits).
   - If the user's provided inputs directly fulfill the scheme's main criteria (e.g. an SC higher-education student earning ₹2 Lakhs applying for Post-Matric SC Scholarship CG028, or an Indian citizen applying for PMJDY CG043), classify it as FULLY_MATCHED with "missing_condition": null.
   - Do NOT demote a direct match merely because of generic administrative phrases like "subject to applicable guidelines" or "procedure applies".
2. POTENTIALLY_RELEVANT:
   - Mark as POTENTIALLY_RELEVANT only when there is a SPECIFIC, UNPROVEN EXTERNAL PREREQUISITE beyond basic demographics, such as:
     * Foreign university offer letter & passport (e.g. National Overseas Scholarship CG026)
     * Admission to a premier notified institution like IIT/NIT/AIIMS (e.g. Top Class Scheme CG027)
     * Selection in official government BPL/deprivation database (e.g. PM-JAY CG013)
     * Household pucca house non-ownership / Urban Local Body selection (e.g. PMAY-U CG011)
     * Choosing a specific vocational trade or project component (e.g. PM-DAKSH CG023, PM-AJAY CG024)
     * Residential rooftop solar connection ownership (e.g. PM Surya Ghar CG049)
     * Bank loan/credit assessment appraisal
   - For POTENTIALLY_RELEVANT, set "missing_condition" to the exact prerequisite that needs external verification.
3. Keep reasons concise (1 sentence) and do not invent requirements outside the database.

Return ONLY a valid JSON object matching this structure:
{{
  "evaluations": [
    {{
      "scheme_id": "CG028",
      "decision": "FULLY_MATCHED",
      "reason": "Direct match for an SC student in higher education with income within scheme norms.",
      "missing_condition": null
    }},
    {{
      "scheme_id": "CG027",
      "decision": "POTENTIALLY_RELEVANT",
      "reason": "Targeted at SC students, but requires admission to a premier notified institution.",
      "missing_condition": "Admission to a notified premier institution (e.g. IIT, NIT, Central University)."
    }}
  ]
}}
"""

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://govschemes.local",
            "X-Title": "Gov Scheme Matcher"
        }

        # max_tokens set to 1500 to keep within token budget
        payload = {
            "model": "google/gemini-2.5-flash",
            "messages": [
                {"role": "system", "content": "You are a precise eligibility analysis engine. Output only valid JSON without markdown formatting."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 1500,
            "temperature": 0.2
        }

        print("\nEvaluating matching schemes with AI advisor...")
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=45)
        response.raise_for_status()

        res_json = response.json()
        raw_text = res_json["choices"][0]["message"]["content"].strip()

        # Clean markdown fences if present
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        elif raw_text.startswith("```"):
            raw_text = raw_text[3:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]

        parsed = json.loads(raw_text.strip())
        return {item["scheme_id"]: item for item in parsed.get("evaluations", [])}

    except requests.exceptions.HTTPError as e:
        print(f"\n[AI Notice] Status code: {e.response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"\n[AI Notice] Network error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"\n[AI Notice] Parse error: {e}")
        return None
    except Exception as e:
        print(f"\n[AI Notice] Error during evaluation: {e}")
        return None


# ==========================================================
# 5. OUTPUT DISPLAY (Practical Mode)
# ==========================================================
def display_results(user, candidate_schemes, evaluations):
    fully_matched = []
    potentially_relevant = []

    for s in candidate_schemes:
        sid = s["scheme_id"]
        eval_data = evaluations.get(sid, {}) if evaluations else {}

        decision = eval_data.get("decision", "").upper()
        if not decision:
            decision = "FULLY_MATCHED" if eval_data.get(
                "match_type") == "Fully Matched" else "POTENTIALLY_RELEVANT"

        reason = eval_data.get("reason") or eval_data.get("why_relevant") or s.get(
            "short_description", "Matches user eligibility profile.")

        missing_cond = eval_data.get("missing_condition")
        db_conds = s.get("eligibility", {}).get("other_conditions", [])

        # In Practical Mode:
        if decision == "FULLY_MATCHED":
            if not missing_cond or str(missing_cond).strip().lower() in ["none", "null", "all criteria met", "none (all criteria met)"]:
                condition_text = "None (Core criteria fully verified based on your profile)"
            else:
                decision = "POTENTIALLY_RELEVANT"
                condition_text = str(missing_cond).strip()
        else:
            if missing_cond and str(missing_cond).strip().lower() not in ["none", "null"]:
                condition_text = str(missing_cond).strip()
            elif db_conds:
                condition_text = ", ".join(db_conds)
            else:
                condition_text = "Subject to official verification"

        record = {
            "id": sid,
            "name": s["scheme_name"],
            "why_relevant": reason,
            "condition": condition_text,
            "required_documents": s.get("required_documents", []),
            "official_url": get_official_url(s)
        }

        if decision == "FULLY_MATCHED":
            fully_matched.append(record)
        else:
            potentially_relevant.append(record)

    # Summary Header
    print("\n" + "=" * 70)
    print("                    SCHEME MATCHING REPORT")
    print("=" * 70)
    print(f"Age: {user['age']} | Gender: {user['gender'].capitalize()} | State: {user['state']} | Residence: {user['residence'].capitalize()}")
    print(
        f"Occupation: {user['occupation'].capitalize()} | Category: {user['category']} | Annual Income: INR {user['annual_income']:,}")
    print(f"Total Eligible Schemes: {len(candidate_schemes)}")
    print(f"  * Fully Matched: {len(fully_matched)}")
    print(f"  * Potentially Relevant: {len(potentially_relevant)}")
    print("=" * 70)

    # 1. Fully Matched
    print("\n" + "#" * 70)
    print("                      [ 1. FULLY MATCHED ]")
    print("#" * 70)
    if not fully_matched:
        print("No schemes in this category.")
    else:
        for idx, item in enumerate(fully_matched, 1):
            print(f"\n[{idx}] {item['name']} ({item['id']})")
            print(f"    * Why relevant: {item['why_relevant']}")
            print(f"    * Additional conditions: {item['condition']}")
            docs_str = ", ".join(
                item['required_documents']) if item['required_documents'] else "Standard KYC"
            print(f"    * Documents required: {docs_str}")
            print(f"    * Official website: {item['official_url']}")

    # 2. Potentially Relevant
    print("\n" + "#" * 70)
    print("                   [ 2. POTENTIALLY RELEVANT ]")
    print("#" * 70)
    if not potentially_relevant:
        print("No schemes in this category.")
    else:
        for idx, item in enumerate(potentially_relevant, 1):
            print(f"\n[{idx}] {item['name']} ({item['id']})")
            print(f"    * Why relevant: {item['why_relevant']}")
            print(f"    * Missing condition: {item['condition']}")
            docs_str = ", ".join(
                item['required_documents']) if item['required_documents'] else "Standard KYC"
            print(f"    * Documents required: {docs_str}")
            print(f"    * Official website: {item['official_url']}")

    print("\n" + "=" * 70)
    print("                 END OF ELIGIBILITY REPORT")
    print("=" * 70 + "\n")


# ==========================================================
# MAIN EXECUTION FLOW
# ==========================================================
def main():
    # 1. Read and validate user input
    user_profile = get_user_input()
    if not user_profile:
        print("Exiting due to invalid input.")
        sys.exit(1)

    # 2. Read OpenRouter API Key quietly from .env
    api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        print("\n[System Error] OPENROUTER_API_KEY is not configured in .env file.")
        sys.exit(1)

    # 3. Load schemes database
    schemes = load_schemes("schemes.json")
    if not schemes:
        sys.exit(1)
    print(f"\nLoaded {len(schemes)} schemes from database.")

    # 4. Basic Matching
    matched_schemes = []
    for s in schemes:
        if match_scheme(user_profile, s):
            matched_schemes.append(s)

    print(f"Basic matching found {len(matched_schemes)} eligible schemes.")
    if not matched_schemes:
        print("No schemes matched the user profile.")
        sys.exit(0)

    # 5. OpenRouter LLM Evaluation
    evaluations = call_openrouter_llm(user_profile, matched_schemes, api_key)
    if not evaluations:
        evaluations = {}

    # 6. Display Structured Output
    display_results(user_profile, matched_schemes, evaluations)


if __name__ == "__main__":
    main()
