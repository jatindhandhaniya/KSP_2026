import ollama # type: ignore

#Here, we have to define the three functions, then define the three tools with their description
#Then, describing the valid stars and then including the tools in tool_functions box.

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

def get_star_luminosity(star_name):
    luminosities = {
        "sun": 1.0,
        "sirius": 25.4,
        "betelgeuse": 126000,
        "proxima centauri": 0.0017
    }
    return luminosities.get(star_name.lower(), "Star not found")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_star_temperature",
            "description": "Call this tool ONLY when the user asks for the surface temperature of a specific star.",
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
            "description": "Call this tool ONLY when the user asks for the distance of a specific star from Earth.",
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
            "name": "get_star_luminosity",
            "description": "Call this tool ONLY when the user asks for the luminosity of a specific star.",
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

valid_stars = ["sun", "sirius", "betelgeuse", "proxima centauri"]

tool_functions = {                  #We need this tool function part so the result can automatically be according to the tool which was called.
    "get_star_temperature": get_star_temperature,
    "get_star_distance": get_star_distance,
    "get_star_luminosity": get_star_luminosity
}

#From here on, the actual code and llm work starts.

question = "What is the temperature,luminosity and distance of Sirius?"

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": question}],
    tools=tools
)

print(response.message)

#If this response has tool calls, then the if statement happens otherwise else statement.
#If this response does not call tools, then the else statement happens.

#Another llm call is only made when a tool call is made but the star was not there.
#Then the other llm just directly responds to it with its own fed data.
#For the else statement, we firstly define the tool result and then draft the messages for the llm.
#And another string named final response which will get printed.

messages = [
        {"role": "system", "content": "Use ONLY the data extracted from the tool calls. Don't go searching yourself."},
        {"role": "user", "content": question},
        {"role": "assistant", "content": "I will use the tool results to answer.", "tool_calls": response.message.tool_calls},   
    ]

#The above messages will get appended as more and more tool calls get added. 
#We can not add arrays in it & so we have to add each tool call one by one.

if response.message.tool_calls:
    for tool_call in response.message.tool_calls:
        function_name = tool_call.function.name
        arguments = tool_call.function.arguments

        if arguments.get("star_name", "").lower() in valid_stars:
            result = tool_functions[function_name](arguments["star_name"])
            tool_result = f"The result is {str(result)}"
            #Always write the tool_result in this format as sometimes llms have issues in interpreting.
        
        else:
            tool_result = f"'{arguments.get('star_name')}' is not in the database. Answer from your own knowledge."

        #After getting each result, we append it to the message and then start the cycle for the next call.
        messages.append({"role": "tool", "content": tool_result, "name": function_name})
        print(f"Tool: {function_name}, Result: {tool_result}")

    #There is always a requirement of refinement in the sentence that we will pass in the next llm, so another llm is used to refine it.

    print(messages)
    final_response = ollama.chat(
        model="llama3.2",
        messages=messages,
        tools=tools
    )

    print(final_response.message.content)

else:
    print(response.message.content)

#The flow is exactly same as the previous file.
#Since we already mentioned about all the tools and defined the tool_functions, we can just do everything in smaller if-else statement.