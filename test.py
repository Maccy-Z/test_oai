
import os
import sys
from openai import OpenAI

def main():
    # Read gateway endpoint and secret from the environment:
    api_base = "http://localhost:8000/api/v1"
    api_key  = "31415" 

    if not api_base or not api_key:
        print("Error: Please set OPENAI_API_BASE and OPENAI_API_KEY", file=sys.stderr)
        sys.exit(1)

    # Instantiate the client
    client = OpenAI(
        api_key=api_key,
        base_url=api_base
    )

    # Choose your Bedrock model here
    model = "anthropic.claude-3-5-sonnet-20240620-v1:0"

    # Chat history
    messages = [
        {"role": "system", "content": "You are an assistant that speaks concisely."},
        {"role": "user",   "content": "Hello from AWS Bedrock via OpenAI API. Who is Grok?"}
    ]

    # Call the chat completion endpoint
    resp = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=512
    )

    # Print out the assistant's reply
    assistant_msg = resp.choices[0].message.content
    print("Assistant:", assistant_msg)


if __name__ == "__main__":
    print("Starting test")
    main()
 
