import openai

# 1. Set your OpenAI API key
openai.api_key = "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"  # Replace with your real API key

# 2. Function to generate a polite email reply
def generate_reply(email_body, sender_name):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You're a helpful and professional email assistant."},
                {"role": "user", "content": f"Write a polite and helpful reply to the following email from {sender_name}:\n\n{email_body}"}
            ]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# 3. Example email content (you can replace with your own or read from a file)
example_email = """
Hi Sheetal,

I hope you're doing well. I wanted to check if you're available for a quick meeting tomorrow regarding the chatbot project. Let me know what time works for you.

Best,
Ankit
"""

sender = "Ankit"

# 4. Generate and print the reply
reply = generate_reply(example_email, sender)
print("\n--- Suggested Reply ---\n")
print(reply)
