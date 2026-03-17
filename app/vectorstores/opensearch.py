from langchain_community.vectorstores import OpenSearchVectorSearch
from langchain_aws import BedrockEmbeddings
from app.config import settings

def get_vector_store():
    embeddings = BedrockEmbeddings(region_name=settings.AWS_REGION)

    return OpenSearchVectorSearch(
        opensearch_url=settings.OPENSEARCH_ENDPOINT,
        index_name=settings.OPENSEARCH_INDEX,
        embedding_function=embeddings
    )