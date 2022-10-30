from fastapi import FastAPI, HTTPException
from brandykitt import generate_branding_snippet, generate_keywords
from mangum import Mangum 
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
MAX_PROMPT_LENGTH = 32
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_snippet_keywords")
async def generate_snippet_keywords(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)

    return {"snippet": snippet, "keywords": keywords}


def validate_input_length(prompt: str):
    if len(prompt) > MAX_PROMPT_LENGTH:
        raise HTTPException(
            400, f"Input text too long, it must not exceed {MAX_PROMPT_LENGTH} characters")
