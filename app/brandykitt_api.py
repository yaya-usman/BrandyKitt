from fastapi import FastAPI, HTTPException
from brandykitt import generate_branding_snippet, generate_keywords
from mangum import Mangum 
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
MAX_SUBJECT_LENGTH = 32
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
