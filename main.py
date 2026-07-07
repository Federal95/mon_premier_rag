from rag import RAG


def main():
    rag = RAG()

    print("Assistant RAG prêt. Tape 'exit' pour quitter.")

    while True:
        question = input("\nQuestion : ")

        if question.lower() in ["exit", "quit", "q"]:
            break

        answer = rag.answer_question(question)
        print("\nRéponse :")
        print(answer)


if __name__ == "__main__":
    main()