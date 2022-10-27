from fastapi import FastAPI, HTTPException
from brandykitt import generate_branding_snippet, generate_keywords
# from dotenv import load_dotenv

# load_dotenv()

app = FastAPI()
MAX_SUBJECT_LENGTH = 32

# @app.get("/generate_snippet")
# async def generate_snippet(subject: str):
#     snippet = generate_branding_snippet(subject)
#     return {"Snippet": snippet}


# @app.get("/generate_keywords")
# async def generate_keywords_api(subject: str):
#     keywords = generate_keywords(subject)
#     return {"Keywords": keywords}


@app.get("/generate_snippet_keywords")
async def generate_snippet_keywords(subject: str):
    validate_input_length(subject)
    snippet = generate_branding_snippet(subject)
    keywords = generate_keywords(subject)

    return {"Branding_snippet": snippet, "Keywords": keywords}


def validate_input_length(subject: str):
    if len(subject) > MAX_SUBJECT_LENGTH:
        raise HTTPException(
            400, f"Input text too long, it must not exceed {MAX_SUBJECT_LENGTH} characters")
