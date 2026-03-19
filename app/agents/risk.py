from app.llm.bedrock import get_llm

def risk_node(state):
    llm = get_llm()
    context = state.get("context", "")
    prompt = f"Context:\n{context}\n\nDecision:\n{state['decision']}\n\nList risks:"
    return {"risk": llm.invoke(prompt).content}