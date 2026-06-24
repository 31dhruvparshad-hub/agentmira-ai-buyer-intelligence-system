# 🏠 AgentMira – AI Buyer Brief Dashboard

AgentMira is an AI powered real estate lead qualification and property matching platform designed to help realtors analyze buyer inquiries, qualify leads, and identify the most relevant MLS listings.

The platform transforms unstructured buyer messages into structured buyer profiles, ranks available properties using a weighted matching engine, identifies missing information, and provides actionable insights through an interactive dashboard.
![a59421ff-9f3b-48ff-955c-cf32bd6eee8a](https://github.com/user-attachments/assets/904c3adf-983e-450c-8345-aa8b36170070)

---

## 🚀 Features

### 🧠 Buyer Profile Extraction
Automatically extracts key buyer requirements from natural language inquiries:

- Buyer Persona
- Budget & Budget Range
- Property Type
- Bedroom Preferences
- Preferred Neighborhoods
- Must-Have Features
- Nice-To-Have Features
- Special Context & Buyer Intent

---

### 🏡 Intelligent Property Matching

Properties are ranked using a weighted scoring engine based on:

- Property Type Match
- Bedroom Compatibility
- Budget Alignment
- Neighborhood Preferences
- Must-Have Amenities
- Nice-To-Have Features

Each recommendation includes a transparent explanation of why it was selected.

---

### 📊 Lead Intelligence

AgentMira automatically generates:

- Lead Quality Score
- Buyer Narrative
- Buyer Insights
- Realtor Insights
- Missing Information Analysis
- Recommended Follow-Up Actions

---

### 🎨 Interactive Dashboard

The Streamlit dashboard provides:

- Executive Summary
- Lead Intelligence Score
- Buyer Narrative
- Buyer Insights
- Realtor Recommendations
- Property Match Cards
- Missing Information Panel

---

## 🏗️ System Architecture

```text
Buyer Inquiry
       │
       ▼
Buyer Profile Extraction
       │
       ▼
Structured Buyer Profile
       │
       ▼
Property Matching Engine
       │
       ▼
Lead Intelligence Layer
       │
       ▼
AgentMira Dashboard
```

---

## 🛠️ Tech Stack

### Backend

- Python
- Pandas
- Pydantic

### AI Layer

- Google Gemini 2.5 Flash
- Prompt Engineering

### Frontend

- Streamlit

---

## 📂 Project Structure

```text
agentmira-ai-buyer-intelligence/
│
├── app.py
├── main.py
├── extractor.py
├── matcher.py
├── property_matcher.py
├── reason_generator.py
├── lead_brief_generator.py
├── buyer_narrative.py
├── prompts.py
├── schemas.py
├── miami_mls_listings.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/agentmira-ai-buyer-intelligence.git

cd agentmira-ai-buyer-intelligence
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Ensure your Gemini API key is not committed to GitHub.

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will open in your browser automatically.

---

## 📋 Example Workflow

### Input

```text
Hi, I'm relocating to Miami for a new job and looking for a 2-3 bedroom condo in Brickell or Downtown Miami. My budget is around $700K and I'd love a building with a gym and balcony.
```

### AgentMira Generates

- Buyer Profile
- Lead Quality Assessment
- Buyer Narrative
- Realtor Insights
- Top Matching MLS Properties
- Missing Information Analysis
- Suggested Follow-Up Recommendations

---

## 🎯 Design Decisions

The project was designed to mirror a real realtor workflow:

1. Receive buyer inquiry
2. Extract structured requirements
3. Match buyer to MLS inventory
4. Identify gaps in information
5. Generate actionable realtor intelligence

The emphasis was on explainability, usability, and extensibility rather than simply returning a list of properties.

---

## 🔮 Future Enhancements

- CRM Integration
- Automated Follow-Up Agent
- Email Draft Generation
- Multi-Agent Realtor Workflows
- Market Intelligence Layer
- Multi-City MLS Support
- Buyer Preference Memory

---

## 📸 Dashboard Preview

Add screenshots here after deployment.

```markdown
![Dashboard](assets/dashboard.png)
```

---

## 👨‍💻 Author

Developed as part of an AI-native real estate workflow project focused on buyer lead qualification, property matching, and realtor decision support.

---
Built with Python, Streamlit, and Gemini 2.5 Flash.
