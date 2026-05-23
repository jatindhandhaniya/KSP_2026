import ollama # type: ignore

question = "What could explain an unusual spike in radio emissions from a distant galaxy?"

for temp in [0.0, 1.0, 2.0]:
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": question}],
        options={"temperature": temp}
    )
    print(f"Temperature {temp}:")
    print(response.message.content)
    print("-" * 50)

#At low temp (0.0), model always picks the most probable next token. Output is repetitive and deterministic.
#At high temp (2.0), model starts picking less probable tokens. Output becomes creative but starts making errors.

#For a scientific hypothesis, the temp should be between 0.3 to 0.7.
#Low enough to stay coherent. 
#High enough to not repeat the most obvious answer every time.

#In temp 0, same prompt will always give the same response (provided same model)
#But even a slightly higher temp can give different responses for same prompt due to the slight randomness introduced. (Butterfly effect)