from langchain_aws import ChatBedrock
from app.config import settings

def get_llm():
    return ChatBedrock(
        model_id=settings.BEDROCK_MODEL,
        region_name=settings.AWS_REGION
    )