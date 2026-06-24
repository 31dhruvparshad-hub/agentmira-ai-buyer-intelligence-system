def generate_lead_brief(
    buyer_profile,
    top_matches
):

    brief = []

    brief.append("=" * 50)
    brief.append("LEAD BRIEF")
    brief.append("=" * 50)

    # Buyer Summary
    brief.append("\nBUYER SUMMARY")
    brief.append("-" * 20)

    brief.append(
        f"Buyer Persona: {buyer_profile.buyer_persona}"
    )

    brief.append(
        f"Budget Target: ${buyer_profile.budget_target:,}"
        if buyer_profile.budget_target
        else "Budget Target: Not specified"
    )

    if buyer_profile.budget_max:
        brief.append(
            f"Budget Maximum: ${buyer_profile.budget_max:,}"
        )

    brief.append(
        f"Preferred Neighborhoods: {', '.join(buyer_profile.preferred_neighborhoods)}"
        if buyer_profile.preferred_neighborhoods
        else "Preferred Neighborhoods: Not specified"
    )

    brief.append(
        f"Property Type: {', '.join(buyer_profile.property_type)}"
        if buyer_profile.property_type
        else "Property Type: Not specified"
    )

    if (
        buyer_profile.bedrooms_min is not None
        and buyer_profile.bedrooms_max is not None
    ):
        brief.append(
            f"Bedrooms: {buyer_profile.bedrooms_min} - {buyer_profile.bedrooms_max}"
        )
    elif buyer_profile.bedrooms_min is not None:
        brief.append(
            f"Minimum Bedrooms: {buyer_profile.bedrooms_min}"
        )

    if buyer_profile.must_have_features:
        brief.append(
            f"Must-Have Features: {', '.join(buyer_profile.must_have_features)}"
        )

    if buyer_profile.nice_to_have_features:
        brief.append(
            f"Nice-To-Have Features: {', '.join(buyer_profile.nice_to_have_features)}"
        )

    # Lead Quality
    brief.append("\nLEAD QUALITY")
    brief.append("-" * 20)

    missing_count = len(buyer_profile.missing_information)

    if missing_count >= 4:
        brief.append(
            "Low confidence match due to limited buyer information."
        )
    elif missing_count >= 1:
        brief.append(
            "Medium confidence match. Additional buyer details would improve recommendations."
        )
    else:
        brief.append(
            "High confidence match."
        )

    # Buyer Context
    if buyer_profile.special_context:

        brief.append("\nBUYER CONTEXT")
        brief.append("-" * 20)

        for item in buyer_profile.special_context:
            brief.append(f"• {item}")

    # Property Recommendations
    brief.append("\nTOP PROPERTY MATCHES")
    brief.append("-" * 20)

    if not top_matches:

        brief.append(
            "No suitable properties found based on the current requirements."
        )

    else:

        for idx, property_ in enumerate(top_matches, start=1):

            brief.append(f"\n{idx}. {property_['listing_id']}")
            brief.append(f"Address: {property_['address']}")
            brief.append(f"Price: ${property_['price']:,}")
            brief.append(f"Match Score: {property_['score']}")

            if property_.get("features"):
                brief.append(
                    f"Features: {property_['features']}"
                )

            brief.append("Why it matches:")

            for reason in property_["match_reasons"]:
                brief.append(f"  ✓ {reason}")

    # Realtor Notes
    brief.append("\nREALTOR NOTES")
    brief.append("-" * 20)

    if buyer_profile.potential_concerns:

        for concern in buyer_profile.potential_concerns:
            brief.append(f"• {concern}")

    else:

        brief.append(
            "No major concerns identified."
        )

    # Missing Information
    if buyer_profile.missing_information:

        brief.append("\nMISSING INFORMATION")
        brief.append("-" * 20)

        for item in buyer_profile.missing_information:
            brief.append(f"• {item}")

    # Suggested Action
    brief.append("\nSUGGESTED NEXT ACTION")
    brief.append("-" * 20)

    if buyer_profile.missing_information:

        brief.append(
            "Contact the buyer to gather missing details, confirm priorities, and validate the recommended properties before scheduling showings."
        )

    else:

        brief.append(
            "Reach out to discuss the recommended properties and schedule property tours."
        )

    return "\n".join(brief)