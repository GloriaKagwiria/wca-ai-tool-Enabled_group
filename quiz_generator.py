# ============================================================
# AI QUIZ GENERATOR — Group Project (Powered by Claude AI)
# ============================================================
# MEMBER 4 — User Input & Validation (R-T-C-C-O)
# ============================================================
#
# COMMIT 1: Create get_topic with Random and Category support (R, T, C)
#
# R = Random topic
# T = Topic (user types their own)
# C = Category (user picks a group)
#
# NOTE: Run this file together with all other member files.
#       The main entry point is member5_main.py
# ============================================================

import random
from member1_setup import RANDOM_TOPICS

# --- Commit 1: Create get_topic with R, T, C support ---

# R — Pick a completely random topic from any category
def get_random_topic():
    category = random.choice(list(RANDOM_TOPICS.keys()))
    topic = random.choice(RANDOM_TOPICS[category])
    print(f"Random topic: [{category}] {topic}")
    return topic, category

# T — User types their own topic
# C — User picks a category and gets a random topic from it
def get_topic():
    print("\n1. Own topic  2. Category  3. Random")
    choice = input("Choose (1/2/3): ").strip()

    if choice == "2":
        # C — Show all categories and let user pick one
        cats = list(RANDOM_TOPICS.keys())
        for i, c in enumerate(cats, 1):
            print(f"  {i}. {c}")
        n = input("Pick number: ").strip()
        if n.isdigit() and 1 <= int(n) <= len(cats):
            cat = cats[int(n) - 1]
            topic = random.choice(RANDOM_TOPICS[cat])
            print(f"Topic: {topic}")
            return topic, cat
        # If invalid input, fall back to random
        return get_random_topic()

    elif choice == "3":
        # R — Fully random topic
        return get_random_topic()

    else:
        # T — User types their own topic
        topic = input("Enter topic: ").strip()
        if not topic:
            print("Cannot be empty.")
            return get_topic()  # ask again if empty
        return topic, "Custom"# ============================================================
# AI QUIZ GENERATOR — Group Project (Powered by Claude AI)
# ============================================================
# MEMBER 4 — User Input & Validation (R-T-C-C-O)
# ============================================================
#
# COMMIT 2: Create get_count to control number of questions (C)
#
# C = Count (how many questions the user wants)
#
# NOTE: This builds on Commit 1. Add this function below get_topic().
# ============================================================

# --- Commit 2: Create get_count ---
# C — Asks how many questions the user wants (1 to 5).
# Capped at 5 to keep token usage low and responses fast.
def get_count():
    n = input("Number of questions (1-5): ").strip()
    if not n.isdigit() or not (1 <= int(n) <= 5):
        print("Enter a number between 1 and 5.")
        return get_count()  # ask again if invalid
    return int(n)
        
# ============================================================
# AI QUIZ GENERATOR — Group Project (Powered by Claude AI)
# ============================================================
# MEMBER 4 — User Input & Validation (R-T-C-C-O)
# ============================================================
#
# COMMIT 3: Create get_difficulty and get_output_file (O)
#
# O = Output file (where to save the JSON)
#
# NOTE: This builds on Commit 1 and 2. Add these functions at the bottom.
# ============================================================

# --- Commit 3: Create get_difficulty and get_output_file ---

# Difficulty validation — only accepts easy, medium, or hard
def get_difficulty():
    d = input("Difficulty (easy/medium/hard): ").lower().strip()
    if d not in ["easy", "medium", "hard"]:
        print("Invalid. Try again.")
        return get_difficulty()  # ask again if invalid
    return d

# O — Output file name where the quiz JSON will be saved
def get_output_file():
    f = input("Output filename (Enter for 'quiz.json'): ").strip()
    if not f:
        f = "quiz.json"
    # Make sure the file always ends in .json
    if not f.endswith(".json"):
        f += ".json"
    return f
    # ============================================================
# AI QUIZ GENERATOR — Group Project (Powered by Claude AI)
# ============================================================
# MEMBER 5 — Main Entry Point & Error Handling
# ============================================================
#
# COMMIT 1: Add display_quiz and save_quiz helper functions
#
# HOW TO RUN THIS PROJECT:
# Make sure all 5 files are in the same folder, then run:
#   python member5_main.py
# ============================================================

import json
from member3_api import generate_quiz
from member4_input import get_topic, get_count, get_difficulty, get_output_file

# --- Commit 1: Add display_quiz and save_quiz helper functions ---

# Prints the quiz neatly in the terminal for the user to read
def display_quiz(quiz_data, topic, difficulty):
    print(f"\n--- QUIZ: {topic.upper()} ({difficulty.upper()}) ---\n")
    for i, q in enumerate(quiz_data, 1):
        print(f"Q{i}: {q['q']}")
        # Loop through each answer option A, B, C, D
        for letter, option in q["o"].items():
            print(f"   {letter}. {option}")
        print(f"   Answer: {q['a']}\n")

# Saves the quiz data to a JSON file with extra metadata
def save_quiz(quiz_data, topic, difficulty, category, output_file):
    output = {
        "topic": topic,
        "category": category,
        "difficulty": difficulty,
        "total_questions": len(quiz_data),
        "questions": quiz_data
    }
    # Write the JSON file with indentation so it's easy to read
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved to: {output_file}")
    
    # ============================================================
# AI QUIZ GENERATOR — Group Project (Powered by Claude AI)
# ============================================================
# MEMBER 5 — Main Entry Point & Error Handling
# ============================================================
#
# COMMIT 2: Wire up all R-T-C-C-O inputs and quiz generation
#
# NOTE: This builds on Commit 1. Add this block below the helper functions.
# ============================================================

import json
from member3_api import generate_quiz
from member4_input import get_topic, get_count, get_difficulty, get_output_file

def display_quiz(quiz_data, topic, difficulty):
    print(f"\n--- QUIZ: {topic.upper()} ({difficulty.upper()}) ---\n")
    for i, q in enumerate(quiz_data, 1):
        print(f"Q{i}: {q['q']}")
        for letter, option in q["o"].items():
            print(f"   {letter}. {option}")
        print(f"   Answer: {q['a']}\n")

def save_quiz(quiz_data, topic, difficulty, category, output_file):
    output = {
        "topic": topic,
        "category": category,
        "difficulty": difficulty,
        "total_questions": len(quiz_data),
        "questions": quiz_data
    }
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved to: {output_file}")

# --- Commit 2: Wire up all R-T-C-C-O inputs and quiz generation ---
# The guard ensures this only runs when the file is executed directly,
# not when it is imported by another script as a module.
if __name__ == "__main__":
    print("=== AI QUIZ GENERATOR (Claude) ===")

    # Collect all inputs from Member 4 (R-T-C-C-O)
    topic, category  = get_topic()       # R = Random, T = Topic, C = Category
    count            = get_count()       # C = Count of questions
    difficulty       = get_difficulty()  # Difficulty level
    output_file      = get_output_file() # O = Output file name

    print("\nGenerating quiz...\n")

    # Generate and display the quiz (error handling added in Commit 3)
    quiz_data = generate_quiz(topic, difficulty, count)
    display_quiz(quiz_data, topic, difficulty)
    save_quiz(quiz_data, topic, difficulty, category, output_file)
    # ============================================================
# AI QUIZ GENERATOR — Group Project (Powered by Claude AI)
# ============================================================
# MEMBER 5 — Main Entry Point & Error Handling
# ============================================================
#
# COMMIT 3: Add try/except error handling for API failures
#
# NOTE: This is the final version of member5_main.py
#       Replace the previous version with this complete file.
# ============================================================

import json
from member3_api import generate_quiz
from member4_input import get_topic, get_count, get_difficulty, get_output_file

def display_quiz(quiz_data, topic, difficulty):
    print(f"\n--- QUIZ: {topic.upper()} ({difficulty.upper()}) ---\n")
    for i, q in enumerate(quiz_data, 1):
        print(f"Q{i}: {q['q']}")
        for letter, option in q["o"].items():
            print(f"   {letter}. {option}")
        print(f"   Answer: {q['a']}\n")

def save_quiz(quiz_data, topic, difficulty, category, output_file):
    output = {
        "topic": topic,
        "category": category,
        "difficulty": difficulty,
        "total_questions": len(quiz_data),
        "questions": quiz_data
    }
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    print("=== AI QUIZ GENERATOR (Claude) ===")

    topic, category  = get_topic()
    count            = get_count()
    difficulty       = get_difficulty()
    output_file      = get_output_file()

    print("\nGenerating quiz...\n")

    # --- Commit 3: Add try/except error handling ---
    try:
        # Call Member 3's API function to generate the quiz
        quiz_data = generate_quiz(topic, difficulty, count)

        # Display the quiz in the terminal
        display_quiz(quiz_data, topic, difficulty)

        # Save the quiz to a JSON file
        save_quiz(quiz_data, topic, difficulty, category, output_file)

    except json.JSONDecodeError:
        # Happens if Claude returns something that isn't valid JSON
        print("Error: Unexpected format returned. Try again.")

    except Exception as e:
        # Catches any other error e.g. no internet, invalid API key
        print(f"Something went wrong: {e}")
