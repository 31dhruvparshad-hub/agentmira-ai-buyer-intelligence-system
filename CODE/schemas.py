from pydantic import BaseModel
from typing import List, Optional

class BuyerProfile(BaseModel):
    buyer_persona: str | None = None

    budget_target: Optional[int] = None
    budget_max: Optional[int] = None

    preferred_neighborhoods: List[str] = []

    property_type: List[str] = []

    bedrooms_min: Optional[int] = None
    bedrooms_max: Optional[int] = None

    must_have_features: List[str] = []
    nice_to_have_features: List[str] = []

    timeline: Optional[str] = None
    urgency: Optional[str] = None

    financing_type: Optional[str] = None

    special_context: List[str] = []

    missing_information: List[str] = []

    potential_concerns: List[str] = []
