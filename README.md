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
```

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure OpenRouter API key

Create a `.env` file in the project folder:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Do not upload the `.env` file to GitHub.

### 3. Run the FastAPI backend

```bash
uvicorn app:app --reload
```

### 4. Open API documentation

Open this in your browser:

```text
http://127.0.0.1:8000/docs
```

The FastAPI Swagger interface can be used to test the `/find-schemes` endpoint.

## Notes

This project is a hackathon MVP.

The scheme matching is based on the user information and the scheme data available in `schemes.json`.

OpenRouter LLM is used to classify matched schemes and provide explanations and additional conditions that may need verification.

Final scheme eligibility should be verified using the applicable official government scheme guidelines and portals.

The scheme matching is based on the user information and the scheme data available in schemes.json.

OpenRouter LLM is used to classify matched schemes and provide explanations and additional conditions that may need verification.

Final scheme eligibility should be verified using the applicable official government scheme guidelines and portals.
