import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}] 
    )
    return response.choices[0].message["content"].strip() 

if __name__ == "__main__":  
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Healthcare Bot:", response)  
