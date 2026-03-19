import pytest
from unittest.mock import patch

# Mock LLM response
class MockLLM:
    def invoke(self, prompt):
        class R:
            content = "mock_output"
        return R()


@pytest.fixture
def mock_llm():
    with patch("app.llm.bedrock.get_llm", return_value=MockLLM()):
        yield


def test_decision_node(mock_llm):
    from app.agents.decision import decision_node

    state = {"query": "test", "context": "ctx"}
    result = decision_node(state)

    assert "decision" in result
    assert result["decision"] == "mock_output"


def test_risk_node(mock_llm):
    from app.agents.risk import risk_node

    state = {"decision": "test", "context": "ctx"}
    result = risk_node(state)

    assert "risk" in result


def test_policy_node(mock_llm):
    from app.agents.policy import policy_node

    state = {"decision": "test", "context": "ctx"}
    result = policy_node(state)

    assert "policy" in result


def test_governance_node(mock_llm):
    from app.agents.governance import governance_node

    state = {"policy": "test", "context": "ctx"}
    result = governance_node(state)

    assert "governance" in result