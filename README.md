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

The matching logic identifies schemes that may be relevant to the user. OpenRouter LLM is then used to provide a simple explanation of why a scheme matches and what additional conditions may need verification.

## Architecture

User Input
→ Python Matching Logic
→ schemes.json
→ Matching Schemes
→ OpenRouter LLM
→ Explanation
→ Final Scheme Report

## Technologies

- Python
- JSON
- OpenRouter API
- GitHub

## Project Structure

```text
scheme-finder/
├── main.py
├── build_schemes.py
├── schemes.json
├── requirements.txt
└── .gitignore
