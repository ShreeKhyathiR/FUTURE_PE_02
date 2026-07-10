from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_ugc_ad(
    business_name,
    business_type,
    product_service,
    target_audience,
    platform,
    tone,
    goal
):
    # Read prompt template
    with open("prompts/ugc_prompt.txt", "r", encoding="utf-8") as file:
        prompt = file.read()

    # Replace placeholders
    prompt = prompt.format(
        business_name=business_name,
        business_type=business_type,
        product_service=product_service,
        target_audience=target_audience,
        platform=platform,
        tone=tone,
        goal=goal
    )

    try:
        response = client.chat.completions.create(
            model="google/gemma-4-26b-a4b-it:free",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert AI marketing strategist and UGC ad copywriter."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.8,
            max_tokens=2500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error generating UGC Ad Pack:\n\n{e}"