from langchain_openai import ChatOpenAI
from search import search_prompt
from dotenv import load_dotenv

load_dotenv()

def main():
    question = input("PERGUNTA: ")
    chain = search_prompt | _get_model()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    response = chain.invoke(question)
    print(f"RESPOSTA: {response.content}")

def _get_model():
    # return ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
    return ChatOpenAI(model="gpt-5-mini", temperature=0.5)

if __name__ == "__main__":
    main()