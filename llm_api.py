import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# API_KEY and genai.configure moved into call_gemini

def call_gemini(prompt: str, model: str = "gemini-pro", max_tokens: int = 256) -> str:
    """
    Calls Google Gemini LLM with the given prompt and returns the response.
    Handles API key configuration internally.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY not configured. LLM call skipped."

    try:
        genai.configure(api_key=api_key)
        model_instance = genai.GenerativeModel(model) # Renamed to avoid conflict
        response = model_instance.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(max_output_tokens=max_tokens)
        )
        if response.candidates:
            if response.prompt_feedback.block_reason:
                return f"Request blocked due to: {response.prompt_feedback.block_reason}"
            return response.text
        else:
            # Check for blocking at the prompt feedback level if candidates are empty
            if response.prompt_feedback and response.prompt_feedback.block_reason:
                return f"Request blocked due to: {response.prompt_feedback.block_reason}. No content generated."
            return "No content generated. The prompt might have been blocked or the response was empty."
    except Exception as e:
        return f"An error occurred during the Gemini API call: {e}"
