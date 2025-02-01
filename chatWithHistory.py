from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = Ollama(model="deepseek-r1:8b")
memory = ConversationBufferMemory(memory_key="chat_history")
prompt = PromptTemplate(
    input_variables=["chat_history", "user_input"],
    template="""
    You are a helpful AI assistant.
    Below is the chat history:{chat_history}
    User: {user_input}
    AI:
    """
)

chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        break

    response = chain.run(user_input=user_input)
    print("AI: ", response)


