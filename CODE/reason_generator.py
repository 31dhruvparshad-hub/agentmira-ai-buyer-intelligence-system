def generate_match_reasons(
    buyer_profile,
    property_row
):

    reasons = []

    # Property Type
    if property_row["property_type"] in buyer_profile.property_type:
        reasons.append(
            f"Matches requested property type ({property_row['property_type']})"
        )

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
            reasons.append(
                f"Meets bedroom requirement ({property_row['bedrooms']} bedrooms)"
            )

    elif buyer_profile.bedrooms_min is not None:
        if property_row["bedrooms"] >= buyer_profile.bedrooms_min:
            reasons.append(
                f"Meets bedroom requirement ({property_row['bedrooms']} bedrooms)"
            )

    # Budget Match
    budget_limit = (
        buyer_profile.budget_target
        or buyer_profile.budget_max
    )

    if budget_limit:
        if property_row["price"] <= budget_limit:
            reasons.append(
                "Within buyer budget"
            )

    # Neighborhood Match
    if (
        buyer_profile.preferred_neighborhoods
        and property_row["neighborhood"]
        in buyer_profile.preferred_neighborhoods
    ):
        reasons.append(
            f"Located in preferred neighborhood ({property_row['neighborhood']})"
        )

    # Property Features
    property_features = [
        feature.strip()
        for feature in property_row["features"].split(";")
    ]

    # Must-Have Features
    for feature in buyer_profile.must_have_features:
        if feature in property_features:
            reasons.append(
                f"Includes requested feature ({feature})"
            )

    # Nice-To-Have Features
    for feature in buyer_profile.nice_to_have_features:
        if feature in property_features:
            reasons.append(
                f"Includes preferred feature ({feature})"
            )

    return reasons