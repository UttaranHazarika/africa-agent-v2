from app.vectorstores.opensearch import get_vector_store

def memory_node(state):
    store = get_vector_store()
    docs = store.similarity_search(state["query"], k=3)
    context = "\n".join([d.page_content for d in docs])
    return {"context": context}