
import logging
import os
from typing import Optional

from google import genai

logger = logging.getLogger(__name__)


def call_llm(prompt: str,max_tokens: Optional[int]=500) ->str:


    try:
        logger.info("calling Gemini LLM with prompt length: %d",len(prompt))
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        if not response or not response.txt:
            logger.warning("Gemini returnede empty responsde")
            return "The AI could not generate a response."
        logger.info("Gemini LLM calls sucessfully")
        return response.text.strip()
    
    except ValueError:
        logger.exception("validation error while calling LLM")
        raise

    except Exception as e:
        logger.exception("error calling Gemini LLm")
        raise Exception(f"failed to get response from LLm:{str(e)}")
    









    if not system_prompt or not user_prompt:
        raise ValueError("system prompt and user prompt cannot be empty")
    
    combined_prompt = (
        "SYSTEM INSTRUCTIONS:\n"
        f"{system_prompt.strip()}\n\n"
        "USER QUERY: \n"
        f"{user_prompt.strip()}"
    )

    return call_llm(combined_prompt)
    








    



