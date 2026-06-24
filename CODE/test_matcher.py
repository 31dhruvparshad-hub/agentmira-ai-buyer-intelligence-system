from schemas import BuyerProfile
from matcher import calculate_match_score

buyer = BuyerProfile(
    buyer_persona="Relocating Professional",
    property_type=["Condo"],
    bedrooms_min=2,
    budget_target=700000,
    preferred_neighborhoods=["Brickell"],
    must_have_features=["Gym"]
)

property_1 = {
    "property_type": "Condo",
    "bedrooms": 3,
    "price": 650000,
    "neighborhood": "Brickell",
    "features": "Pool; Gym; Balcony"
}

score = calculate_match_score(
    buyer,
    property_1
)

print(score)