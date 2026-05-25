import ollama # type: ignore

#FEW SHOT PROMPTING

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": """Respond with one word only: Positive, Negative, or Neutral. Classify the sentiment of these sentences.

Examples:
Sentence: The food was amazing and the service was great.
Sentiment: Positive

Sentence: I waited an hour and the food was cold.
Sentiment: Negative

Sentence: The meal was okay, nothing special.
Sentiment: Neutral

Sentence: The telescope captured stunning images of the nebula.
Sentiment:"""}
    ],
    options={"temperature": 0}
)

print(response.message.content)

#Here, some examples are given to show the pattern that the LLM would recognize and respond according to that.
#This is called FEW SHOT PROMPTING

#When the pattern or format is custom, unfamiliar, or too specific to describe in words, that's when few-shot examples become necessary

#CHAIN OF THOUGHT

response2 = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": """A star has a surface temperature of 3200K and a luminosity 
0.001 times that of the Sun. What type of star is it?"""}
    ],
    options={"temperature": 0}
)

print(response2.message.content)
#This prints a normal llm response.

response3 = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": """A star has a surface temperature of 3200K and a luminosity 
0.001 times that of the Sun. What type of star is it?

Think step by step:
1. What does the temperature tell us?
2. What does the luminosity tell us?
3. Where does this place it on the HR diagram?
4. Final classification."""}
    ],
    options={"temperature": 0}
)
#This will print the whole chain of thought with retracable steps that can be used to verify if the steps were right or not.
# It's the mechanism that makes an LLM's output auditable. When your agent generates a hypothesis, the reasoning trail is what a reviewer evaluates.

print(response3.message.content)

#System prompt design at research level.

weak_prompt = """You are an astronomy assistant."""

strong_prompt = """You are a stellar classification agent operating inside a multi-agent astronomy pipeline.

Your role: classify stars based on observational data only.

Input you will receive: surface temperature in Kelvin, luminosity relative to the Sun.

Your constraints:
- Base conclusions only on the provided values, not assumptions
- If data is insufficient for confident classification, say so explicitly
- Never speculate beyond what the data supports

Output format:
- Classification: [star type]
- Confidence: [High / Medium / Low]
- Reasoning: [one sentence referencing the specific values provided]"""

data = "Temperature: 3200K, Luminosity: 0.001 solar"

for prompt in [weak_prompt, strong_prompt]:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Classify this star: {data}"}
        ],
        options={"temperature": 0}
    )
    print(f"Prompt type: {'WEAK' if prompt == weak_prompt else 'STRONG'}")
    print(response.message.content)
    print("-" * 50)

#In real system prompt design, we have to provide a role, constraints, input that you will get, output format.
#The big section saying everything is passed as a system prompt while the user prompt only contains the data.
#The data that is passed is given separately by a separaete string.
#This prompt makes the response parseable, predictable & defensible.