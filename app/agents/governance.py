from app.llm.bedrock import get_llm

def governance_node(state):
    llm = get_llm()
    context = state.get("context", "")
    policy = state.get("policy", "")
    prompt = f"Context:\n{context}\n\nPolicy:\n{policy}\n\nGovernance:"
    return {"governance": llm.invoke(prompt).content}