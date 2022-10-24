import os
import openai
import argparse
from dotenv import load_dotenv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    generate_branding_snippet(user_input)


def generate_branding_snippet(subject: str):

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Generate upbeat branding snippet for {subject}"

    response = openai.Completion.create(
        model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=35)
    branding_text = response["choices"][0]["text"]
    last_char = branding_text[-1]

    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    print(branding_text)


if __name__ == "__main__":
    load_dotenv()
    main()
