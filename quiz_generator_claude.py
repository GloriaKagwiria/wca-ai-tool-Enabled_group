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
