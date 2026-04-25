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
    topic = "world science"
    difficulty = "medium"

Generate 5 {difficulty} difficulty question about {topic}.

### Role
are an expert educator who creates quizzes for students. Your task is to generate 5 questions about the topic of {topic} at the {difficulty} difficulty level. Each question should be clear, concise, and relevant to the topic. 
### Task
Generate a set of 5 multiple choice questions (MCQs) based on a specific topic and difficulty level.
### Context
Topic: {topic}
Difficulty:[easy, medium, hard]
### Constraints
1. Each question must have 4 answer options (A, B, C, D).
2. Structure: Each question should be followed by its answer options, and the correct answer should be indicated.
3. Difficulty Levels:
 - Easy: Basic recall questions that test fundamental knowledge of the topic.    - Medium: Questions that require some application of knowledge and understanding of concepts.
- Hard: Questions that require critical thinking and synthesis of informion from multiple sources.
4. Accuracy: Ensure that all questions and answers are factually correct and relevant to the specified topic.
### Output Format
Return the response strictly in the following JSON format:
```json
{
  "questions": [
    {
      "question": "Question text here",
      "options": {
        "A": "string",
        "B": "string",
        "C": "string",
        "D": "string"
      },
      "correct_answer": "A"  // Indicate the correct option (A, B, C, or D)
    },
    // Repeat for each of the 5 questions
  ]
}
```
    """
    return prompt



def generate_quiz(topic, difficulty):
    prompt = build_prompt(topic, difficulty)

    # Send the request to Claude via the Anthropic API
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the text content from Claude's response
    return message.content[0].text

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
