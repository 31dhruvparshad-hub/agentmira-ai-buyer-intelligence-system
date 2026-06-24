def generate_buyer_narrative(
    buyer
):

    budget = buyer.budget_target or buyer.budget_max

    narrative = (
        f"This lead is categorized as a "
        f"{buyer.buyer_persona.lower()} seeking "
        f"{', '.join(buyer.property_type)} properties"
    )

    if budget:
        narrative += (
            f" with a budget around ${budget:,}."
        )
    else:
        narrative += " with an unspecified budget."

    if buyer.bedrooms_min:
        narrative += (
            f" The buyer prefers at least "
            f"{buyer.bedrooms_min} bedrooms."
        )

    if buyer.special_context:
        narrative += (
            " Additional context: "
            + ", ".join(buyer.special_context)
            + "."
        )

    return narrative