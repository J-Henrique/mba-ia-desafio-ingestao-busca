from langchain_google_genai import ChatGoogleGenerativeAI

from search import search_prompt
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
    question = input("Pergunta: ")
    chain = search_prompt(question)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    # model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
    response = model.invoke(chain)
    print(response.content)

if __name__ == "__main__":
    main()