from google import genai
import os
from dotenv import load_dotenv

load_dotenv()



def enhance_pitch_with_ai(pitch):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found.")
    
    client = genai.Client(api_key=api_key)

    prompt = f"""
    You are a professional career pitch editor.

    Rewrite the following pitch into ONE single professional paragraph.
    Do NOT add headings.
    Do NOT add bullet points.
    Do NOT add sections like 'Key Features' or explanations.
    Do NOT change the meaning.
    Keep it concise, impactful, and natural.
    Return only the final improved pitch.

    Pitch:
    {pitch}
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )


    return response.text