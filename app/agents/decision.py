from app.llm.bedrock import get_llm

def decision_node(state):
    llm = get_llm()
    return {"decision": llm.invoke(state["query"]).content}