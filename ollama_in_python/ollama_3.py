import ollama # type: ignore

prompts = [
    "What causes stars to die?",
    "You are an astrophysicist. What causes stars to die?",
    "You are an astrophysicist explaining to a 10 year old. What causes stars to die?",
    "You are a skeptical scientist. List only what is observationally confirmed about stellar death. No speculation."
]

for prompt in prompts:
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.3}
    )
    print(f"Prompt: {prompt[:60]}...")
    print(response.message.content)
    print("-" * 50)