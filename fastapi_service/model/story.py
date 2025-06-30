import openai
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv(dotenv_path="/Users/akash/Documents/GitHub/Microservice-based-AI-Image-Captioning-Web-App/key.env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#openai.api_key = os.getenv("OPEN_API_KEY")

def generate_story_from_caption(caption : str) -> str:
    prompt = {
        f"Write a short and imaginative story based on this image caption:\n"
        f"'{caption}'\n"
        "Keep it under 5 sentences."
    }

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=150,
        )

        story = response.choices[0].message.content.strip()
        return story
    
    except Exception as e:
        return f"(Story generation failed: {e})"