import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

#Each message has a role:-
#User -> What I send to find results on
#Assistant -> What the model responds to my prompt.
#System -> Background instructions that shape how the model behaves throughout

print(response)                     #This will give a lot of output like time,date, etc.
print(response.message.content)     #This will give the content part of the message part of the response which is the actual response.

response1 = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "You are a skeptical scientist who questions everything. Keep answers under 3 sentences."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response1.message.content)
#I'm not convinced that the answer is Paris, as I've seen discrepancies in historical records and some claim it was actually Chartres at one point. Nevertheless, according to most recent sources, Paris remains the commonly accepted capital of France.

#Here, the model says that he is not convinced and has seen discrepancies. But it hasn't seen any discrepancies.
#It is just providing skepticism because I told it to, not because there's actual skepticism.
#This is HALLUCINATION in a subtle form.

messages1 = [
    {"role": "system", "content": "You are a helpful assistant. Keep answers under 2 sentences."},
    {"role": "user", "content": "My name is Jatin."},
]       #We can draft a message like this and use it whenever we want to.

response2 = ollama.chat(model="llama3.2", messages=messages1)
print(response2.message.content)            #Here we are giving it the user content, to get a generic response, there is no question.

messages1.append({"role": "assistant", "content": response2.message.content})       #We are now appending the response earlier to our message
messages1.append({"role": "user", "content": "What is my name?"})               #We are now adding the question as the user so it only replies to that

response3 = ollama.chat(model="llama3.2", messages=messages1)   
print(response3.message.content)            #Your name is Jatin.

#Here, the assistant message is added so there are two user messages together or else the LLM will see it as two questions.
#The llm can only see one message at a time so it is necessary to explain the whole history to it to get better results.

#Now, let's make the whole chatting loop

messages3 = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")

    if user_input == "quit":
        break
    else:
        messages3.append({"role": "user", "content":user_input})

        response4 = ollama.chat(model="llama3.2", messages=messages3)
        reply = response4.message.content

        messages3.append({"role": "assistant", "content":reply})

        print(f"Assistant: {reply}\n")


        print(f"Messages in history: {len(messages3)}")         #Through this, we see the message count is like 3,5,7,9 and so on

#Here, I have made a fully functioning chatbot. 
#The if break statement was necessary to break out of the loop or else it would just keep going on and on.

#CONTEXT WINDOW
#For llama3.2, the hard limit of tokens of which it can keep track of is 128,000. 
#Even under the limit, the more history we send, the slower the response will become.

#CONVERSATION SUMMAARISATION
#We periodically compress the whole history into a summary and keep replacing
#But on compression, the real depth of the conversation gets lost.

#In deep research work, an external memory is used to store the full history outside the model, retrieve only what's relevant when needed.
#This is what RAG solves.

