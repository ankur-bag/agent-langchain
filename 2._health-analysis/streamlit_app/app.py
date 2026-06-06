from dotenv import load_dotenv
import os
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="Blood Work Analyzer",
    layout="wide"
)

# Gemini 2.5 Flash Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)

# Custom CSS
st.markdown("""
<style>
.scroll-box {
    height: 230px;
    overflow-y: auto;
    padding: 12px 16px;
    border: 1px solid #333;
    border-radius: 8px;
    background-color: #1e1e1e;
    font-size: 0.9rem;
    line-height: 1.6;
    color: #e0e0e0;
}

.scroll-box p,
.scroll-box li {
    color: #e0e0e0;
}

.section-label {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 6px;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🩸 Blood Work Analyzer")

# Layout
left_col, right_col = st.columns([1, 1])

# Left Column
with left_col:

    st.subheader("Blood Work Report")

    blood_report = st.text_area(
        label="Paste your report below",
        height=500,
        placeholder="Paste your blood work report here...",
        label_visibility="collapsed"
    )

    analyze_clicked = st.button(
        "Analyze",
        type="primary",
        use_container_width=True
    )

# Right Column
with right_col:

    st.subheader("Health Summary")

    health_box = st.empty()

    health_box.markdown(
        '<div class="scroll-box"></div>',
        unsafe_allow_html=True
    )

    st.subheader("Suggested Diet Plan")

    diet_box = st.empty()

    diet_box.markdown(
        '<div class="scroll-box"></div>',
        unsafe_allow_html=True
    )

# Analyze Logic
if analyze_clicked:

    if not blood_report.strip():

        st.warning("Please paste a blood work report before analyzing.")

    else:

        with st.spinner("Analyzing your blood work..."):

            try:

                # STEP 1 — Extract and classify values
                extraction_prompt = f"""
You are a medical data extraction assistant.

From the blood report below:

1. Extract ALL test values.
2. Compare them with the reference ranges.
3. Classify each value as:
   - HIGH
   - LOW
   - NORMAL

Format strictly like this:

- Test Name: value | Status: HIGH/LOW/NORMAL | Reference: range

Blood Report:
{blood_report}
"""

                extraction_response = llm.invoke(extraction_prompt)

                extracted_values = extraction_response.content

                # STEP 2 — Generate summary + Indian diet plan
                diet_prompt = f"""
You are a clinical nutritionist specializing in Indian diets.

Based on the blood work analysis below, generate TWO sections.

SECTION 1 - HEALTH SUMMARY:
- Explain the patient's condition in simple language.
- Use 4-5 concise lines.
- Avoid heavy medical jargon.

SECTION 2 - INDIAN DIET PLAN:
Provide:
1. Foods to eat more of
2. Foods to avoid

Use practical Indian foods like:
- dal
- roti
- sabzi
- rice
- paneer
- fruits
- curd
etc.

Keep the advice concise and practical.

Blood Work Analysis:
{extracted_values}
"""

                diet_response = llm.invoke(diet_prompt)

                full_response = diet_response.content

            except Exception as e:

                st.error(f"Error: {e}")

                st.stop()

        # Split Sections
        if "SECTION 2" in full_response:

            parts = full_response.split("SECTION 2")

            health_summary = (
                parts[0]
                .replace("SECTION 1 - HEALTH SUMMARY:", "")
                .replace("SECTION 1", "")
                .strip()
            )

            diet_plan = (
                ("SECTION 2" + parts[1])
                .replace("SECTION 2 - INDIAN DIET PLAN:", "")
                .replace("SECTION 2", "")
                .strip()
            )

        else:

            health_summary = full_response
            diet_plan = "Diet plan could not be generated."

        # Render Health Summary
        health_box.markdown(
            f"""
<div class="scroll-box">
{health_summary}
</div>
""",
            unsafe_allow_html=True
        )

        # Render Diet Plan
        diet_box.markdown(
            f"""
<div class="scroll-box">
{diet_plan}
</div>
""",
            unsafe_allow_html=True
        )