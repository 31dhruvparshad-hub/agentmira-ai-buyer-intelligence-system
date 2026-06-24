from schemas import BuyerProfile

MATCH_WEIGHTS = {
    "property_type": 30,
    "bedrooms": 25,
    "budget": 25,
    "neighborhood": 15,
    "must_have_feature": 10,
    "nice_to_have_feature": 5
}


def calculate_match_score(
    buyer_profile: BuyerProfile,
    property_row
):
    score = 0

    # Property Type Match
    if property_row["property_type"] in buyer_profile.property_type:
        score += MATCH_WEIGHTS["property_type"]

    # Bedroom Match
    if (
        buyer_profile.bedrooms_min is not None
        and buyer_profile.bedrooms_max is not None
    ):
        if (
            buyer_profile.bedrooms_min
            <= property_row["bedrooms"]
            <= buyer_profile.bedrooms_max
        ):
            score += MATCH_WEIGHTS["bedrooms"]

    elif buyer_profile.bedrooms_min is not None:
        if property_row["bedrooms"] >= buyer_profile.bedrooms_min:
            score += MATCH_WEIGHTS["bedrooms"]

    # Budget Match
    budget_limit = None

    if buyer_profile.budget_target:
        budget_limit = buyer_profile.budget_target

    elif buyer_profile.budget_max:
        budget_limit = buyer_profile.budget_max

    if budget_limit:
        if property_row["price"] <= budget_limit:
            score += MATCH_WEIGHTS["budget"]

    # Neighborhood Match
    if (
        buyer_profile.preferred_neighborhoods
        and property_row["neighborhood"] in buyer_profile.preferred_neighborhoods
    ):
        score += MATCH_WEIGHTS["neighborhood"]

    # Property Features
    property_features = [
        feature.strip()
        for feature in property_row["features"].split(";")
    ]

    # Must-Have Feature Match
    for feature in buyer_profile.must_have_features:
        if feature in property_features:
            score += MATCH_WEIGHTS["must_have_feature"]

    # Nice-To-Have Feature Match
    for feature in buyer_profile.nice_to_have_features:
        if feature in property_features:
            score += MATCH_WEIGHTS["nice_to_have_feature"]

    return score