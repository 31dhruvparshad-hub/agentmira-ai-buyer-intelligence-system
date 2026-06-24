import pandas as pd

from extractor import extract_buyer_profile
from property_matcher import get_top_matches
from lead_brief_generator import generate_lead_brief


def process_lead(
    buyer_message,
    df
):
    buyer_profile = extract_buyer_profile(
        buyer_message
    )

    top_matches = get_top_matches(
        buyer_profile,
        df
    )

    lead_brief = generate_lead_brief(
        buyer_profile,
        top_matches
    )

    return lead_brief


# NEW FUNCTION FOR DASHBOARD UI
def process_lead_dashboard(
    buyer_message,
    df
):
    buyer_profile = extract_buyer_profile(
        buyer_message
    )

    top_matches = get_top_matches(
        buyer_profile,
        df
    )

    lead_brief = generate_lead_brief(
        buyer_profile,
        top_matches
    )

    return {
        "buyer_profile": buyer_profile,
        "top_matches": top_matches,
        "lead_brief": lead_brief
    }


if __name__ == "__main__":

    df = pd.read_csv(
        "miami_mls_listings.csv"
    )

    lead = """
    Hi, I'm relocating to Miami for a new job at a tech company and I'm looking for a 2-3 bedroom condo in Brickell or Downtown Miami. Budget is around $700K, ideally with a gym in the building and a balcony with a city view. Move-in needed by August.
    """

    result = process_lead(
        lead,
        df
    )

    print(result)