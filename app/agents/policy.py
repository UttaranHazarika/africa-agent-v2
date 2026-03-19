from app.llm.bedrock import get_llm

def policy_node(state):
    llm = get_llm()
    context = state.get("context", "")
    prompt = f"Context:\n{context}\n\nDecision:\n{state['decision']}\n\nPolicies:"
    return {"policy": llm.invoke(prompt).content}