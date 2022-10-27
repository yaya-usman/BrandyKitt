import os
from typing import List
import openai
import argparse
import re
from dotenv import load_dotenv

load_dotenv()


MAX_SUBJECT_LENGTH = 32


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    if validate_length(user_input):
        generate_branding_snippet(user_input)
        generate_keywords(user_input)
    else:
        raise ValueError(
            f"Your input must not exceed {MAX_SUBJECT_LENGTH} characters")


def validate_length(subject: str) -> bool:
    return len(subject) <= MAX_SUBJECT_LENGTH


def generate_branding_snippet(subject: str) -> str:

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Generate upbeat branding snippet for {subject}"

    response = openai.Completion.create(
        model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=35)

    # Extracting and cleaning text from response
    branding_text: str = response["choices"][0]["text"]
    branding_text = branding_text.strip()

    last_char = branding_text[-1]

    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    print(f"Branding_Text: {branding_text}")
    return branding_text


def generate_keywords(subject: str) -> List[str]:

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Generate unique related branding keywords for {subject}"

    response = openai.Completion.create(
        model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=35)

    # Extracting and cleaning text from response
    keywords_text: str = response["choices"][0]["text"]
    keywords_text = keywords_text.strip()
    keywordsList = re.split(",|-|\n", keywords_text)

    # strip off extra spaces, ignore empty string and remove digits in the list if it exist
    keywordsList = [re.sub('[0-9.]', '', i).lower().strip()
                    for i in keywordsList]

    keywordsList = [k for k in keywordsList if len(k) > 0]

    print(f"Branding_Keywords: {keywordsList}")
    return keywordsList


if __name__ == "__main__":
    main()
