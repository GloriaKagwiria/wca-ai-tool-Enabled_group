def build_prompt(topic,difficulty):
    prompt = f"""
Generate 5 {difficulty} difficulty question about {topic}.
Difficulty level: {difficulty}

Rules:
1. Each question should be clear and concise.
2. Avoid using ambiguous language.
3. Each question must have 4 options (A, B, C, D) with only one correct answer.
4. The correct answer should be indicated clearly.
5. Avoid using technical jargon unless necessary.
6. Make questions appropriate for the specified difficulty level.
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
