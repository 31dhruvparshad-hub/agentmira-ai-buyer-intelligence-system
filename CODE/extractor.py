from google import genai
from schemas import BuyerProfile
from prompts import EXTRACTION_PROMPT
from normalizer import normalize_features

client = genai.Client(api_key="AQ.Ab8RN6JA7iyAOAmRO1tvmKfJvdpmcfJFe3WqU5nmVr29fI8iQw")

def extract_buyer_profile(message: str):

    prompt = f"""
    {EXTRACTION_PROMPT}

    Buyer Inquiry:
    {message}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    result = response.text.strip()

    # Remove markdown fences if present
    result = result.replace("```json", "").replace("```", "").strip()

    profile = BuyerProfile.model_validate_json(result)

    # Normalize features
    profile.must_have_features = normalize_features(
        profile.must_have_features
    )

    profile.nice_to_have_features = normalize_features(
        profile.nice_to_have_features
    )

    return profile