from langgraph.graph import StateGraph, END
from app.agents.decision import decision_node
from app.agents.risk import risk_node
from app.agents.policy import policy_node
from app.agents.governance import governance_node
from app.agents.memory import memory_node

class AgentState(dict):
    query: str
    context: str | None = None
    decision: str | None = None
    risk: str | None = None
    policy: str | None = None
    governance: str | None = None


builder = StateGraph(AgentState)

builder.add_node("memory", memory_node)
builder.add_node("decision", decision_node)
builder.add_node("risk", risk_node)
builder.add_node("policy", policy_node)
builder.add_node("governance", governance_node)

builder.set_entry_point("memory")

builder.add_edge("memory", "decision")
builder.add_edge("decision", "risk")
builder.add_edge("decision", "policy")
builder.add_edge("policy", "governance")

def final_node(state):
    return {
        "final": f"""
Decision:
{state.get('decision')}

Risk:
{state.get('risk')}

Policy:
{state.get('policy')}

Governance:
{state.get('governance')}
"""
    }

builder.add_node("final", final_node)

builder.add_edge(["risk", "governance"], "final")
builder.add_edge("final", END)

graph = builder.compile()