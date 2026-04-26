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
        return topic, "Custom"
