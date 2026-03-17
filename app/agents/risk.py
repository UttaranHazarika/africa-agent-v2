from app.llm.bedrock import get_llm

def risk_node(state):
    llm = get_llm()
    return {"risk": llm.invoke(f"Risks: {state['decision']}").content}