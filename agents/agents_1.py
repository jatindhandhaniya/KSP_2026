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

tool_functions = {
    "get_star_temperature": get_star_temperature,
    "get_star_distance": get_star_distance
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_star_temperature",
            "description": "Get the surface temperature of a specific star in Kelvin.",
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
            "description": "Get the distance of a specific star from Earth in light years.",
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

question = "Is Sirius hotter than the Sun? If yes, how far is it from Earth?"

messages = [
    {"role": "system", "content": "You are an astronomy assistant. Use tools to find accurate data. Reason step by step. When you have enough data to answer the question, give a final answer. Call tools ONLY when you are sure what to call, don't call randomly."},
    {"role": "user", "content": question}
]

print(f"Question: {question}\n")

#Below is the whole react loop
#Firstly, we define the number of max iterations so that the loop doesn't go on forever consuming tokens. 

max_iterations = 5
iteration = 0

while iteration < max_iterations:
    iteration += 1
    print(f"\n--- Iteration {iteration} ---")

    #The above part will tell which iteration is going on throughout the processing.

    response = ollama.chat(
        model="llama3.2",
        messages=messages,
        tools=tools
    )
    
    #The above is the only llm that will run in this whole loop

    if response.message.tool_calls:
        messages.append({"role": "assistant","content": "","tool_calls": response.message.tool_calls})
        
        #This if is used to append the tool calls which were made 

        #The below for loop is used to add the called data to the messages for the next run.
        #Each tool call is getting handled separately so that there is no confusion in reasoning.

        for tool_call in response.message.tool_calls:
            function_name = tool_call.function.name
            arguments = tool_call.function.arguments
            result = tool_functions[function_name](arguments["star_name"])
            
            print(f"Tool: {function_name}({arguments['star_name']}) → {result}")
            
            messages.append({"role": "tool","content": str(result),"name": function_name})
    
    else:
        print(f"\nFinal Answer: {response.message.content}")
        break

    if iteration == max_iterations:
        print("Max iterations reached — agent stopped.")

#--- Iteration 1 ---
#Tool: get_star_temperature(Sirius) → 9940
#Tool: get_star_distance(Sun) → 0
#Tool: get_star_temperature(Sun) → 5778
#--- Iteration 2 ---
#Final Answer: Sirius is actually hotter than the Sun, with a surface temperature of around 9,900 Kelvin (9,627°C or 17,442°F). However, it's not as far from Earth as the Sun. Sirius is approximately 8.6 light-years away from our planet.

#The above was the result, notice the 8.6 light years was not called by the tool, it's slient failure.
#For this we will need the verifiablility score. We will implement this later.