
if __name__ == "__main__":
    topic = get_topic()
    difficulty = get_difficulty()

    print("\nGenerating your quiz, please wait...\n")

    try:
        quiz = generate_quiz(topic, difficulty)
        print("--- QUIZ ---\n")
        print(quiz)
    except Exception as e:
        print(f"Something went wrong: {e}")