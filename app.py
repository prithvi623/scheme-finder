from fastapi import FastAPI
from pydantic import BaseModel
import os
import main

app = FastAPI(title="Government Scheme Finder API")


class UserProfile(BaseModel):
    age: int
    gender: str
    state: str
    residence: str
    occupation: str
    education: str
    category: str
    annual_income: float


@app.get("/")
def home():
    return {
        "message": "Government Scheme Finder API is running"
    }


@app.post("/find-schemes")
def find_schemes(user: UserProfile):

    user_profile = {
        "age": user.age,
        "gender": user.gender.lower(),
        "state": user.state,
        "residence": user.residence.lower(),
        "occupation": user.occupation.lower(),
        "education": user.education.lower(),
        "category": user.category.upper(),
        "annual_income": user.annual_income,
        "is_farmer": "farmer" in user.occupation.lower(),
        "is_student": "student" in user.occupation.lower()
        or "student" in user.education.lower()
    }

    # Load database
    schemes = main.load_schemes("schemes.json")

    if not schemes:
        return {
            "error": "Could not load schemes.json"
        }

    # Basic matching
    matched_schemes = []

    for scheme in schemes:
        if main.match_scheme(user_profile, scheme):
            matched_schemes.append(scheme)

    if not matched_schemes:
        return {
            "user": user_profile,
            "total_matched": 0,
            "fully_matched": [],
            "potentially_relevant": []
        }

    # OpenRouter API key
    api_key = os.getenv("OPENROUTER_API_KEY", "").strip()

    if not api_key:
        return {
            "error": "OPENROUTER_API_KEY is not configured"
        }

    # LLM evaluation
    evaluations = main.call_openrouter_llm(
        user_profile,
        matched_schemes,
        api_key
    )

    if not evaluations:
        evaluations = {}

    fully_matched = []
    potentially_relevant = []

    # Create API response
    for scheme in matched_schemes:

        scheme_id = scheme["scheme_id"]

        evaluation = evaluations.get(scheme_id, {})

        decision = evaluation.get("decision", "").upper()

        reason = (
            evaluation.get("reason")
            or evaluation.get("why_relevant")
            or scheme.get(
                "short_description",
                "Matches the user profile."
            )
        )

        missing_condition = evaluation.get(
            "missing_condition"
        )

        documents = scheme.get(
            "required_documents",
            []
        )

        official_url = main.get_official_url(scheme)

        result = {
            "scheme_id": scheme_id,
            "scheme_name": scheme["scheme_name"],
            "why_relevant": reason,
            "missing_condition": missing_condition,
            "documents": documents,
            "official_url": official_url
        }

        if decision == "FULLY_MATCHED":
            fully_matched.append(result)
        else:
            potentially_relevant.append(result)

    return {
        "user": user_profile,
        "total_matched": len(matched_schemes),
        "fully_matched": fully_matched,
        "potentially_relevant": potentially_relevant
    }
