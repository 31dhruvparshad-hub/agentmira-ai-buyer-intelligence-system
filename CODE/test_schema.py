from schemas import BuyerProfile

profile = BuyerProfile(
    buyer_persona="Relocating Professional",
    budget_target=700000,
    property_type=["Condo"]
)

print(profile)