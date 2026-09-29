# Government Scheme Finder

An AI-powered Government Scheme Finder developed as a hackathon MVP.

## What it does

The application collects basic citizen information such as:

- Age
- Gender
- State
- Residence
- Occupation
- Education
- Category
- Annual household income

It compares the user's profile with government scheme data stored in `schemes.json`.

The matching logic identifies schemes that may be relevant to the user. OpenRouter LLM is then used to classify and provide a simple explanation of why a scheme matches and what additional conditions may need verification.

The FastAPI backend provides the scheme results as a JSON response so that a frontend application can use them.

## Architecture

User Input → FastAPI Backend → Python Matching Logic → schemes.json → Matching Schemes → OpenRouter LLM → Explanation → JSON Response → Frontend

## Technologies

- Python
- JSON
- FastAPI
- OpenRouter API
- Requests
- python-dotenv
- Uvicorn
- GitHub

## Project Structure

```text
scheme-finder/
├── main.py
├── app.py
├── build_schemes.py
├── schemes.json
├── requirements.txt
├── .gitignore
└── README.md
