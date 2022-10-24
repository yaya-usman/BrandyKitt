import os
from typing import List
import openai
import argparse
import re
from dotenv import load_dotenv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    branding_result = generate_branding_snippet(user_input)
    keywords_result = generate_keywords(user_input)
    print(branding_result)
    print(keywords_result)


def generate_branding_snippet(subject: str) -> str:

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Generate upbeat branding snippet for {subject}"

    response = openai.Completion.create(
        model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=35)
    
    #Extracting and cleaning text from response 
    branding_text: str = response["choices"][0]["text"]
    branding_text = branding_text.strip()

    last_char = branding_text[-1]

    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    return branding_text


def generate_keywords(subject: str) -> List[str]:

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Generate unique related branding keywords for {subject}"

    response = openai.Completion.create(
        model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=35)
    
    #Extracting and cleaning text from response 
    keywords_text: str = response["choices"][0]["text"]
    keywords_text = keywords_text.strip()
    keywordsList = re.split(",|-|\n", keywords_text)
    keywordsList = [k.lower().strip() for k in keywordsList if len(k) > 0]

    return keywordsList


if __name__ == "__main__":
    load_dotenv()
    main()
