import ollama # type: ignore

def get_star_temperature(star_name):
    temperatures = {
        "sun": 5778,
        "sirius": 9940,
        "betelgeuse": 3500,
        "proxima centauri": 3042
    }
    return temperatures.get(star_name.lower(), "Star not found")

def get_star_distance(star_name):
    distances = {
        "sun": 0,
        "sirius": 8.6,
        "betelgeuse": 700,
        "proxima centauri": 4.24
    }
    return distances.get(star_name.lower(), "Star not found")

stars = ["sun", "sirius", "betelgeuse", "proxima centauri"]

tools=[
        {
            "type": "function",
            "function": {
                "name": "get_star_temperature",
                "description": "Call this tool to get the surface temperature of a specific star.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "star_name": {"type": "string", "description": "The name of the star"}
                    },
                    "required": ["star_name"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_star_distance",
                "description": "Call this tool to get the distance of a specific star from Earth in light years.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "star_name": {"type": "string", "description": "The name of the star"}
                    },
                    "required": ["star_name"]
                }
            }
        }
    ]

print("STEP 1: Getting temperatures")

hot_stars = []

for star in stars:
    temp = get_star_temperature(star)
    print(f"{star}: {temp}K")
    if temp != "Star not found" and temp > 5000:
        hot_stars.append(star)

print(f"\nStars above 5000K: {hot_stars}")

print("\nSTEP 2: Getting distances for hot stars")

for star in hot_stars:
    distance = get_star_distance(star)
    print(f"{star}: {distance} light years")


print("\nSTEP 3: LLM-driven chain")

question = "Which stars in this list are hotter than 5000K, and how far are they from Earth? Stars: sun, sirius, betelgeuse, proxima centauri"

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": question}],
    tools=tools
)

print(response.message.tool_calls)
#

tool_functions = {
    "get_star_temperature": get_star_temperature,
    "get_star_distance": get_star_distance
}

messages = [
    {"role": "user", "content": question},
    {"role": "assistant", "content": "", "tool_calls": response.message.tool_calls}
]

if response.message.tool_calls:
    for tool_call in response.message.tool_calls:
        function_name = tool_call.function.name
        arguments = tool_call.function.arguments
        result = tool_functions[function_name](arguments["star_name"])
        messages.append({"role": "tool", "content": str(result), "name": function_name})
        print(f"Tool: {function_name}({arguments['star_name']}) → {result}")

    #Here, we can see that Tool: 
    #get_star_temperature(sun) → 5778
    #get_star_temperature(sirius) → 9940
    #get_star_distance(betelgeuse) → 700
    #The llm could not reason everything about which tools to call and when. 
    #The model got confused because the tool calls were inconsistent and it tried to reason across mismatched results.

    #That's where the ReAct loop comes in. The model :- Reasons about what to do next
    #Makes one tool call
    #Observes the result
    #Reasons again based on that result
    #Repeats until done