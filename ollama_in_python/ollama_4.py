import ollama  # type: ignore
import json

#JSON is a way to structure data such that both the computer and human can understand.
#when an agent returns a response as plain prose, another agent can't programmatically extract specific pieces from it. You need structured data.

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": """Give me 3 facts about black holes.
Return your response as JSON only, in this exact format:
{
    "facts": [
        {"id": 1, "title": "fact title", "description": "fact description"},
        {"id": 2, "title": "fact title", "description": "fact description"},
        {"id": 3, "title": "fact title", "description": "fact description"}
    ]
}
Return nothing else. No explanation, no preamble. Just the JSON."""}
    ],
    options={"temperature": 0}
)

#Here, I am giving the model a template to fill in exactly. By writing the last line. It only gives the desired content.
#But the model can not prepare even the perfect output even after creating such a big prompt.
#The model ran out of tokens or lost track of structure mid-generation. Even at temperature 0.
#This is a fundamental limitation and can not be cured by a better prompt.

#So, instead of the big prompt, we are using another feature.

#This code is just to find the exact invalid statement
try:        
    data = json.loads(response.message.content)
    for fact in data["facts"]:
        print(fact["title"])
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
    print(response.message.content)

#STRUCTURED OUTPUTS
#Here, we are going to force JSON by constraining its generation at token level.
#In this, only valid JSON tokens will be left to select from after each token.
#It removes all the other tokens from consideration.
#This is called constrained decoding.

response1 = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Give me 3 facts about black holes."}
    ],
    format={
        "type": "object",
        "properties": {
            "facts": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "title": {"type": "string"},
                        "description": {"type": "string"}
                    }
                }
            }
        }
    },
    options={"temperature": 0.3}
)

data1 = json.loads(response1.message.content)
#If data1 loads correctly, this means the response is a successful JSON.

print(response1.message.content)

for fact in data1["facts"]:
    print(fact["title"])

#In here, we did not give any big message. We just constrained everything in one JSON format and output came accordingly.
#This is the right way for cross LLM communication as if the structure is a prose, then we need to parse it, then error handling and so on.
#The pipeline becomes fragile at every step.

#So, Guaranteed structure = reliable code = trustworthy pipeline.
