import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Interview Question Generator",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Interview Question Generator")
st.write("Generate role-specific interview questions using Generative AI.")

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# User inputs
job_role = st.text_input(
    "Job Role",
    placeholder="e.g., Software Development Engineer Intern"
)

skills = st.text_input(
    "Skills",
    placeholder="e.g., Python, SQL, OOP, Data Structures"
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

number_of_questions = st.selectbox(
    "Number of Technical Questions",
    [5, 10, 15]
)

# Generate button
if st.button("🚀 Generate Questions"):

    # Check API key
    if not api_key:
        st.error(
            "Gemini API key is missing. Please add GEMINI_API_KEY to your .env file."
        )
        st.stop()

    # Check inputs
    if not job_role or not skills:
        st.warning("Please enter both the job role and skills.")
        st.stop()

    # Create Gemini client
    client = genai.Client(api_key=api_key)

    # Prompt
    prompt = f"""
You are an expert technical interviewer.

Generate an interview preparation set for the following candidate:

Job Role: {job_role}
Skills: {skills}
Difficulty: {difficulty}

Generate exactly {number_of_questions} technical interview questions.

For every technical question, provide:
1. Question
2. Short and clear answer
3. Brief explanation

After the technical questions, generate exactly 3 behavioral/HR interview
questions with suggested answers.

Make the questions relevant to the specified job role and skills.

Use clear headings and numbered sections.
Keep answers concise and suitable for a student preparing for an interview.
"""

    # Call Gemini
    try:
        with st.spinner("Generating interview questions..."):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        # Display result
        st.success("Questions generated successfully!")

        st.markdown("## 📚 Interview Questions")
        st.markdown(response.text)

    except Exception as e:
        st.error("Something went wrong while contacting the Gemini API.")
        st.write("Error:", str(e))