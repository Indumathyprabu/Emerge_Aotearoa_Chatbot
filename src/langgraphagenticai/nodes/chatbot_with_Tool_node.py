from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration (no Tavily fallback).
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])
        tools_response = f"Tool integration for: '{user_input}'"
        return {"messages": [llm_response, tools_response]}

    def create_chatbot(self, tools):
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            user_input = state["messages"][-1] if state["messages"] else ""
            try:
                tool_response = llm_with_tools.invoke(state["messages"])
                if not tool_response or not getattr(tool_response, "content", "").strip():
                    raise ValueError("Tool returned empty or blank content.")
            except Exception as e:
                print(f"[WARN] Tool failed: {e}")
                tool_response = self.llm.invoke(state["messages"])

            return {"messages": [tool_response]}

        return chatbot_node
