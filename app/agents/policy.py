from app.llm.bedrock import get_llm

def policy_node(state):
    llm = get_llm()
    return {"policy": llm.invoke(f"Policies: {state['decision']}").content}