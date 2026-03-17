import os

class Settings:
    AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
    BEDROCK_MODEL = os.getenv("BEDROCK_MODEL", "anthropic.claude-3")

    OPENSEARCH_ENDPOINT = os.getenv("OPENSEARCH_ENDPOINT")
    OPENSEARCH_INDEX = os.getenv("OPENSEARCH_INDEX", "africa-index")

settings = Settings()