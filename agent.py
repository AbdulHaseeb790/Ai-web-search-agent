from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

load_dotenv(dotenv_path='D:\web-search-agent\.env')

llm = ChatGroq(model='llama-3.1-8b-instant')
search_tool = TavilySearchResults(max_results=3)
tools = [search_tool]
memory = InMemorySaver()
agent = create_react_agent(llm, tools, checkpointer=memory, prompt="You are a helpful AI research assistant. Use the search tool to find accurate and up-to-date information. Always provide clear, detailed, and well-structured answers.")

def ask_agent(user_input, thread_id="1"):
    config = {'configurable': {'thread_id': thread_id}}
    response = agent.invoke(
        {'messages': [{'role': 'user', 'content': user_input}]},
        config=config
    )
    return response['messages'][-1].content