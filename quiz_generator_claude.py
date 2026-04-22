#==============================================================
# QUIZ GENERATOR- ENABLED GROUP-PROJECT(Powered by claude AI)
# Members : 1(Setup) |2 (Prompt) |3 (API) |4(Input) |5(Main)
# How to run : python quiz_generator.py
#===============================================================

#===============================================================
# Member 1- Project Setup $ API Configuration
# Commit 1: Add project imports
# Commit 2: Configure anthropic client using environment variable
# Commit 3: Add project-level documentation and header comments
#================================================================

import anthropic
import os

# The API key is loaded from the environment variable ANTHROPIC_API_KEY
# To set it permanently, run : setx ANTHROPIC_API_KEY "your_key_here"
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))






def build_prompt(topic,difficulty):
    prompt = f"""
Generate 5 {difficulty} difficulty question about {topic}.
Difficulty level: {difficulty}

Rules:
1. Each question should be clear and concise.
2. Avoid using ambiguous language.
3. Each question must have 4 options (A, B, C, D) with only one correct answer.
4. The correct answer should be indicated clearly.
5. Make questions appropriate for the specified difficulty level.
- Easy: Basic knowledge and understanding of the topic.
- Medium: Requires application of knowledge and some critical thinking.
- Hard: Requires deep understanding and analysis of the topic.
"""
    return prompt

# Commit 1: Create the get_topic function
# .strip() removes accidental spaces before or after the input
def get_topic():
    topic = input("Enter topic: ").strip()
    return topic
# Commit 2: Add empty input validation with recursive retry
# If the user presses Enter without typing anything, the function
# calls itself again recursively until a valid topic is provided.
def get_topic():
    topic = input("Enter topic: ").strip()
    if not topic:
        print("Topic cannot be empty.")
        return get_topic()  # ask again if empty
    return topic
# Commit 3: Create get_difficulty function with validation
# .lower() means "Easy", "EASY", and "easy" all work the same
# Reject anything that isn't one of the three valid options
def get_difficulty():
    difficulty = input("Enter difficulty (easy, medium, hard): ").lower().strip()
    if difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty. Please enter easy, medium, or hard.")
        return get_difficulty()  # ask again if invalid
    return difficulty



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
        
        #Final version ready for review

