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
