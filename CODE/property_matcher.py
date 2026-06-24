import pandas as pd

from reason_generator import generate_match_reasons
from matcher import calculate_match_score


def get_top_matches(
    buyer_profile,
    df,
    top_k=3
):

    matches = []

    budget_limit = (
        buyer_profile.budget_target
        or buyer_profile.budget_max
    )

    for _, row in df.iterrows():

        # Budget Filter
        if budget_limit:
            if row["price"] > budget_limit * 1.2:
                continue

        # Property Features
        property_features = [
            feature.strip()
            for feature in row["features"].split(";")
        ]

        # Must-Have Feature Filter
        if buyer_profile.must_have_features:

            missing_feature = False

            for feature in buyer_profile.must_have_features:

                if feature not in property_features:
                    missing_feature = True
                    break

            if missing_feature:
                continue

        score = calculate_match_score(
            buyer_profile,
            row
        )
        if score < 30:
         continue

        reasons = generate_match_reasons(
            buyer_profile,
            row
        )

        matches.append({
            "listing_id": row["listing_id"],
            "address": row["address"],
            "score": score,
            "price": row["price"],
            "neighborhood": row["neighborhood"],
            "features": row["features"],
            "match_reasons": reasons
        })

    matches = sorted(
        matches,
        key=lambda x: x["score"],
        reverse=True
    )

    return matches[:top_k]