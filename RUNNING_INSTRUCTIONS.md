# 🚀 How to Run AgentMira

This guide explains how to run AgentMira on your computer, even if you have never worked with Python before.

## Prerequisites

Before running the project, make sure the following software is installed on your computer:

### 1. Install Python

Version

Python 3.11.0


### 2. Download the Project

Either:

* Clone the GitHub repository

```bash
git clone <repository-url>
```

or

* Download the repository as a ZIP file from GitHub and extract it.

---

## Project Setup

Open Terminal (Mac/Linux) or Command Prompt (Windows).

Navigate to the project folder:

```bash
cd agentmira-ai-buyer-intelligence
```

---

### Install Required Libraries

Run:

```bash
pip install -r requirements.txt
```

This will automatically install all required dependencies.

---

## Configure Gemini API Key

AgentMira uses Google's Gemini model to extract information from buyer inquiries.

Open the file:

```text
extractor.py
```

Replace the API key placeholder with your own Gemini API key.

A Gemini API key can be obtained from:

https://aistudio.google.com/

---

## Run the Application

Start the Streamlit dashboard:

```bash
streamlit run app.py
```

After a few seconds, Streamlit will display a local URL similar to:

```text
http://localhost:8501
```

Open this URL in your web browser.

---

## Using AgentMira

1. Paste a buyer inquiry into the text box.
2. Click **Generate Lead Brief**.
3. AgentMira will:

   * Extract buyer requirements
   * Generate a buyer profile
   * Score MLS properties
   * Recommend matching properties
   * Identify missing information
   * Provide realtor insights

---

## Example Buyer Inquiry

```text
Hi, I'm relocating to Miami for a new job and looking for a 2-3 bedroom condo in Brickell or Downtown Miami. Budget is around $700K. Ideally I would like a gym and a balcony. Move-in needed by August.
```

---

## Expected Output

The dashboard will display:

* Lead Intelligence Score
* Buyer Narrative
* Executive Summary
* Buyer Insights
* Realtor Insights
* Matching MLS Properties
* Follow-Up Recommendations

---

## Troubleshooting

### Module Not Found Error

Run:

```bash
pip install -r requirements.txt
```

again to ensure all dependencies are installed.

### Streamlit Not Found

Run:

```bash
pip install streamlit
```

### Browser Does Not Open Automatically

Open the URL shown in the terminal manually:

```text
http://localhost:8501
```

---

If the application launches successfully and displays the AgentMira dashboard, the setup is complete.
