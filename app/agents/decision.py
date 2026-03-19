from app.llm.bedrock import get_llm

def decision_node(state):
    llm = get_llm()
    context = state.get("context", "")
    prompt = f"Context:\n{context}\n\nQuery:\n{state['query']}"
    return {"decision": llm.invoke(prompt).content}



