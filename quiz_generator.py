# ============================================================
# AI QUIZ GENERATOR — Group Project (Powered by Claude AI)
# ============================================================
# MEMBER 2 — Prompt Engineering
# ============================================================
#
# COMMIT 3: Add difficulty-level instructions to prompt
#
# NOTE: This is the final version of member2_prompt.py
#       Replace the previous version with this complete file.
# ============================================================

from member1_setup import RANDOM_TOPICS

def build_prompt(topic, difficulty, count):

    # --- Commit 2: Add compact JSON format instructions ---
    # We tell Claude to reply ONLY in JSON so we can parse it easily.
    # Short JSON keys like "q", "o", "a" save extra output tokens too.

    # --- Commit 3: Add difficulty-level instructions ---
    # Passing difficulty inside the prompt tells Claude how hard
    # the questions should be — easy, medium, or hard.
    return (
        f"Make {count} MCQ on {topic}, difficulty={difficulty}. "
        f"Reply ONLY in JSON array:\n"
        f'[{{"q":"?","o":{{"A":"","B":"","C":"","D":""}},"a":"A"}}]'
    )
# ============================================================
# AI QUIZ GENERATOR — Group Project (Powered by Claude AI)
# ============================================================
# MEMBER 3 — API Call & Response Handling
# ============================================================
#
# COMMIT 1: Create generate_quiz function skeleton
#
# NOTE: Run this file together with all other member files.
#       The main entry point is member5_main.py
# ============================================================

import json
from member1_setup import client
from member2_prompt import build_prompt

# --- Commit 1: Create generate_quiz function skeleton ---
# This function takes topic, difficulty and count as inputs
# and returns a list of quiz questions parsed from JSON.
def generate_quiz(topic, difficulty, count):
    pass  # logic will be added in Commit 2 and Commit 3
# ============================================================
# AI QUIZ GENERATOR — Group Project (Powered by Claude AI)
# ============================================================
# MEMBER 3 — API Call & Response Handling
# ============================================================
#
# COMMIT 2: Send prompt to Claude API using haiku model (600 tokens)
#
# NOTE: This builds on Commit 1. Replace the pass with this code.
# ============================================================

import json
from member1_setup import client
from member2_prompt import build_prompt

def generate_quiz(topic, difficulty, count):

    # --- Commit 2: Send prompt to Claude API ---
    # We use claude-haiku — the cheapest and fastest Claude model.
    # max_tokens=600 limits how long Claude's response can be,
    # keeping API costs low while still fitting 1-5 questions.
    prompt = build_prompt(topic, difficulty, count)
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text  # raw text — JSON parsing added in Commit 3
# ============================================================
# AI QUIZ GENERATOR — Group Project (Powered by Claude AI)
# ============================================================
# MEMBER 3 — API Call & Response Handling
# ============================================================
#
# COMMIT 3: Clean and parse JSON response from Claude
#
# NOTE: This is the final version of member3_api.py
#       Replace the previous version with this complete file.
# ============================================================

import json
from member1_setup import client
from member2_prompt import build_prompt

def generate_quiz(topic, difficulty, count):
    prompt = build_prompt(topic, difficulty, count)
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}]
    )

    # --- Commit 3: Clean and parse JSON response ---
    # Sometimes Claude adds a small amount of extra text before or
    # after the JSON. We find the "[" and "]" to extract only the
    # JSON array and then parse it into a Python list.
    raw = message.content[0].text
    start = raw.find("[")
    end = raw.rfind("]") + 1
    quiz_data = json.loads(raw[start:end])
    return quiz_data
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
