import cohere

# Paste your API key here
co = cohere.Client("hS8P2Ncshdsh8SDrRggwoZ0kjzD5qyu72zSLeTQI")

# Sample long email thread
email_thread = """
Hi Team, Just wanted to follow up on the proposal. We had a meeting scheduled with the client next week, and I’d like to finalize things by Friday.

Hey, the design team shared updated mockups. They're attached. Please review and give feedback by Thursday.

Following up, the legal team had a few concerns about the third-party terms. I've added their comments to the shared doc.

All, final version is now in the drive. Let me know if I should proceed to send it.
"""

# Use Cohere's command model to summarize and interpret intent
prompt = f"""You are an AI assistant that summarizes email threads.
Email Thread:
\"\"\"
{email_thread}
\"\"\"
Summarize the thread briefly and extract the main intent or action item.

Respond in this format:
- Summary:
- Intent:
"""

response = co.generate(
    model='command-r-plus',  # Use command-r-plus if you have access
    prompt=prompt,
    max_tokens=300,
    temperature=0.5
)

print("\n🧠 Cohere LLM Output:\n")
print(response.generations[0].text.strip())
