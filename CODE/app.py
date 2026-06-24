import streamlit as st
import pandas as pd

from buyer_narrative import generate_buyer_narrative
from main import process_lead_dashboard

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
    page_title="AgentMira(Buyer Briefer)",
    page_icon="🏠",
    layout="wide"
)

# ==================================================
# Custom CSS
# ==================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #E5E7EB;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

.stTextArea textarea {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# Load Data
# ==================================================

df = pd.read_csv("miami_mls_listings.csv")

# ==================================================
# Sidebar
# ==================================================

with st.sidebar:

    st.title("🏠 Agent Mira")

    st.markdown("---")

    st.markdown("### Features")

    st.write("✅ Buyer Persona Detection")
    st.write("✅ Property Matching")
    st.write("✅ Lead Qualification")
    st.write("✅ Realtor Insights")
    st.write("✅ Follow-Up Recommendations")

    st.markdown("---")

    st.caption("Powered by Gemini 2.5 Flash")

# ==================================================
# Header
# ==================================================

st.markdown("""
<div style='text-align:center;padding:10px'>
    <h1>🏠 AgentMira</h1>
    <h4 style='color:gray'>
        AI-Powered Buyer Briefer Dashboard
    </h4>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==================================================
# Input
# ==================================================

lead_message = st.text_area(
    "📥 Paste Buyer Inquiry",
    height=220,
    placeholder="Paste Inquiry"
)

# ==================================================
# Main Logic
# ==================================================

if st.button("Generate Lead Brief", use_container_width=True):

    if lead_message.strip():

        with st.spinner("Analyzing buyer inquiry..."):

            result = process_lead_dashboard(
                lead_message,
                df
            )

        buyer = result["buyer_profile"]
        matches = result["top_matches"]

        st.success("Lead Analysis Complete")

        # ==================================================
        # Lead Score
        # ==================================================

        missing_count = len(
            buyer.missing_information
        )

        lead_score = max(
            50,
            100 - (missing_count * 10)
        )

        st.subheader("🎯 Lead Intelligence Score")

        if lead_score >= 80:
            st.success(
                f"🟢 {lead_score}/100 - High Quality Lead"
            )

        elif lead_score >= 60:
            st.warning(
                f"🟡 {lead_score}/100 - Qualified Lead"
            )

        else:
            st.error(
                f"🔴 {lead_score}/100 - Needs More Information"
            )

        # ==================================================
        # Buyer Narrative
        # ==================================================

        st.subheader("📝 Buyer Narrative")

        st.info(
            generate_buyer_narrative(
                buyer
            )
        )

        # ==================================================
        # Executive Summary
        # ==================================================

        st.subheader("📋 Executive Summary")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Buyer Persona",
                buyer.buyer_persona
            )

        with col2:
            st.metric(
                "Budget",
                f"${buyer.budget_target or buyer.budget_max:,}"
                if (buyer.budget_target or buyer.budget_max)
                else "N/A"
            )

        with col3:
            st.metric(
                "Property Type",
                ", ".join(buyer.property_type)
            )

        with col4:

            bedrooms = (
                f"{buyer.bedrooms_min}-{buyer.bedrooms_max}"
                if buyer.bedrooms_max
                else str(buyer.bedrooms_min)
            )

            st.metric(
                "Bedrooms",
                bedrooms
            )

        st.divider()

        # ==================================================
        # Insights Section
        # ==================================================

        left, right = st.columns(2)

        with left:

            st.subheader("🧠 Buyer Insights")

            if buyer.special_context:

                for item in buyer.special_context:
                    st.write(f"• {item}")

            else:

                st.info(
                    "No buyer insights available."
                )

        with right:

            st.subheader("🚨 Realtor Insights")

            if buyer.potential_concerns:

                for concern in buyer.potential_concerns:
                    st.warning(concern)

            else:

                st.success(
                    "No major concerns identified."
                )

        st.divider()

        # ==================================================
        # Property Matches
        # ==================================================

        st.subheader("🏡 Top Property Matches")

        cols = st.columns(3)

        for idx, property_ in enumerate(matches[:3]):

            score = property_["score"]

            with cols[idx]:

                st.markdown(
                    f"### {property_['listing_id']}"
                )

                if score >= 90:

                    st.success(
                        f"Match Score: {score}"
                    )

                elif score >= 70:

                    st.warning(
                        f"Match Score: {score}"
                    )

                else:

                    st.error(
                        f"Match Score: {score}"
                    )

                st.write(
                    f"📍 {property_['address']}"
                )

                st.write(
                    f"🏘️ {property_['neighborhood']}"
                )

                st.write(
                    f"💰 ${property_['price']:,}"
                )

                st.markdown(
                    "**Features**"
                )

                features = property_[
                    "features"
                ].split(";")

                for feature in features[:5]:

                    st.write(
                        f"🏷️ {feature.strip()}"
                    )

                st.markdown(
                    "**Why It Matches**"
                )

                for reason in property_[
                    "match_reasons"
                ]:

                    st.write(
                        f"✅ {reason}"
                    )

        st.divider()

        # ==================================================
        # Recommended Follow-Up
        # ==================================================

        st.subheader("📞 Recommended Follow-Up")

        if buyer.missing_information:

            for idx, item in enumerate(
                buyer.missing_information,
                start=1
            ):

                st.write(
                    f"{idx}. Clarify {item}"
                )

        else:

            st.success(
                "Buyer profile appears complete."
            )

        # ==================================================
        # Missing Information
        # ==================================================

        if buyer.missing_information:

            with st.expander(
                "⚠️ Missing Information"
            ):

                for item in buyer.missing_information:

                    st.write(
                        f"• {item}"
                    )

        # ==================================================
        # AgentMira Recommendation
        # ==================================================
        
        st.subheader(
            "💡 AgentMira Recommendation"
        )
        
        if buyer.missing_information:
        
            st.info(
                f"Current matches provide a strong starting point. Clarifying {len(buyer.missing_information)} remaining buyer details could improve match accuracy and help identify properties that are more closely aligned with the buyer's goals."
            )
        
        else:
        
            st.success(
                "The buyer profile appears well-defined and the recommended properties align closely with the stated requirements. This may be a good opportunity to discuss specific listings and potential next steps."
            )