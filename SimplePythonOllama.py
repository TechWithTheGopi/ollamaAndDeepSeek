from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1:8b")

result = model.invoke("What is ollama?")

print(result)
