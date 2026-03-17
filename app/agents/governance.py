from app.llm.bedrock import get_llm

def governance_node(state):
    llm = get_llm()
    return {"governance": llm.invoke(f"Governance: {state['policy']}").content}