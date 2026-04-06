from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, description="The question to ask the AI")


class AskResponse(BaseModel):
    answer: str = Field(..., description="The AI-generated answer")


class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=1, description="The text to summarize")


class SummarizeResponse(BaseModel):
    summary: str = Field(..., description="The summarized text")


class ContextAskRequest(BaseModel):
    question: str = Field(..., min_length=1, description="The question to ask")
    context: str = Field(..., min_length=1, description="The context for answering")


class HealthResponse(BaseModel):
    status: str = Field(default="healthy", description="Service health status")
    version: str = Field(default="1.0.0", description="API version")