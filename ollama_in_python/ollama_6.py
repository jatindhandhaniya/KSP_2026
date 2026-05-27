import ollama # type: ignore

def get_star_temperature(star_name):
    temperatures = {
        "sun": 5778,
        "sirius": 9940,
        "betelgeuse": 3500,
        "proxima centauri": 3042
    }
    return temperatures.get(star_name.lower(), "Star not found")

#This is a defined function that would get the name of the star, convert it to lower case and return the temp accordingly.

tools=[
        {
            "type": "function",     #This is the type of tool, function or image analysis or whatever.
            "function": {
                "name": "get_star_temperature",     #This must be same as the function name.
                "description": "Call this tool ONLY when the user asks for the surface temperature of a specific star by name.",        
                #This is where we explain what the tool does and other constraints.
                "parameters": {         #This explains about the inputs of the tool
                    "type": "object",   #The inputs as objects
                    "properties": {            
                        "star_name": {      #One input is star name
                            "type": "string",   #The type of the star name is string
                            "description": "The name of the star"
                        }
                    },
                    "required": ["star_name"]       #The only required input for this tool is star name
                }
            }
        }
    ]

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "What is the surface temperature of Sirius?"}
    ],
    tools=tools
)

print(response.message)         

tool_call = response.message.tool_calls[0]          #Make the 1st tool call a separate string

function_name = tool_call.function.name             #Define the tool call's name and arguements
arguments = tool_call.function.arguments

result = get_star_temperature(arguments["star_name"])   #This is what the tool call actually brought result.
print(f"Tool result: {result}")                         #We can directly work with this result but we need more LLMs for further tasks with this result.

messages = [
    {"role": "user", "content": "What is the surface temperature of Sirius?"},
    {"role": "assistant", "content": "", "tool_calls": response.message.tool_calls},        #Here, the assistant's job is only to run the tool call, nothing else
    {"role": "tool", "content": str(result), "name": "get_star_temperature"}                #Here, the content is only the result of the tool call and the name explains from which function it came from.
]                                                                                           

#The goal of this response is not to do the tool call but to understand the context of the tool call made along with the question.

final_response = ollama.chat(
    model="llama3.2",
    messages=messages,
    tools=tools
)

#This will finally print the exact answer to our first question.

print(final_response.message.content)

#SILENT FAILURE AND VALIDATION

response3 = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "What is a red dwarf?"}
    ],
    tools=tools
)

#Sometimes the model calls the tool even when it doesn't need to.
#This is called silent failure — no crash, but wrong behavior.
#We first check if a tool call was even made before trying to extract it.

if response3.message.tool_calls:
    arguments3 = response3.message.tool_calls[0].function.arguments

    valid_stars = ["sun", "sirius", "betelgeuse", "proxima centauri"]

    if arguments3.get("star_name", "").lower() not in valid_stars:
        #The star name provided is not in our database — invalid tool call.
        #Instead of crashing or silently failing, we tell the model to use its own knowledge.
        
        fallback_message = f"'{arguments3.get('star_name')}' is not in the database. Answer from your own knowledge."

        messages3 = [
            {"role": "user", "content": "What is a red dwarf?"},
            {"role": "assistant", "content": "", "tool_calls": response3.message.tool_calls},
            #The tool result message contains the fallback instruction instead of real data.
            {"role": "tool", "content": fallback_message, "name": "get_star_temperature"}
        ]

        final_response3 = ollama.chat(
            model="llama3.2",
            messages=messages3,
            tools=tools
        )

        print(final_response3.message.content)

    else:
        #Valid tool call — star exists in database, execute normally.
        result3 = get_star_temperature(arguments3["star_name"])
        print(f"Tool result: {result3}")

else:
    #Model answered directly without calling any tool — no validation needed.
    print("No tool call made. Direct response:")
    print(response3.message.content)