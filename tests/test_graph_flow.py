from unittest.mock import patch

class MockLLM:
    def invoke(self, prompt):
        class R:
            content = "mock_output"
        return R()


def test_graph_flow():
    with patch("app.llm.bedrock.get_llm", return_value=MockLLM()), \
         patch("app.agents.memory.memory_node", return_value={"context": "mock_context"}):

        from app.graph.graph import graph

        state = {"query": "test"}

        result = graph.invoke(state)

        assert result is not None