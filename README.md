# AI Interview Question Generator 🤖

An AI-powered web application that generates role-specific technical and behavioral interview questions using Google's Gemini API.

## Project Overview

The AI Interview Question Generator helps students and job seekers prepare for technical interviews. Users enter a job role, required skills, and difficulty level, and the application uses Generative AI to create relevant interview questions with answers and explanations.

## Features

* Generate technical interview questions
* Generate short answers and explanations
* Generate behavioral/HR questions
* Select interview difficulty
* Select the number of technical questions
* Role-specific question generation
* Simple and interactive Streamlit interface
* Error handling for missing API keys and API failures

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* Generative AI
* Prompt Engineering
* python-dotenv

## How It Works

1. The user enters a job role and relevant skills.
2. The user selects the difficulty level and number of questions.
3. The application creates a structured prompt using the provided information.
4. The prompt is sent to Google's Gemini model through the Gemini API.
5. Gemini generates technical and behavioral interview questions.
6. The generated questions and answers are displayed in the Streamlit application.

## Installation

Clone the repository or download the project.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your Gemini API key.

## How to Run

Run the following command:

```bash
streamlit run app.py
```

The application will open in your browser.

## Future Improvements

* Add resume upload and analysis
* Add interview question categories
* Add a mock interview mode
* Add question history
* Add answer evaluation using Generative AI
* Add difficulty-based scoring
* Add support for multiple AI models
