from fastapi import APIRouter, HTTPException
import logging

from app.models.schemas import (
    AskRequest,
    AskResponse,
    SummarizeRequest,
    SummarizeResponse,
    ContextAskRequest
)
from app.services.llm import call_llm
from app.services.prompts import (
    system_prompt,
    QA_prompt_template,
    SUMMARY_PROMPT_TEMPLATE,
    CONTEX_QA_PROMPT_TEMPLATE
)

router = APIRouter(prefix="/ai", tags=["AI"])
logger = logging.getLogger(__name__)


@router.post("/ask", response_model=AskResponse)
async def ask_question(request: AskRequest):
    try:
        prompt = QA_prompt_template.format(function=request.question)
        answer = call_llm(prompt)
        return AskResponse(answer=answer)
    except Exception as e:
        logger.error(f"Error in ask endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process question")


@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_text(request: SummarizeRequest):
    try:
        prompt = SUMMARY_PROMPT_TEMPLATE.format(text=request.text)
        summary = call_llm(prompt)
        return SummarizeResponse(summary=summary)
    except Exception as e:
        logger.error(f"Error in summarize endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to summarize text")


@router.post("/ask-with-context", response_model=AskResponse)
async def ask_with_context(request: ContextAskRequest):
    try:
        prompt = CONTEX_QA_PROMPT_TEMPLATE.format(
            contex=request.context,
            question=request.question
        )
        answer = call_llm(prompt)
        return AskResponse(answer=answer)
    except Exception as e:
        logger.error(f"Error in ask-with-context endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process question with context")