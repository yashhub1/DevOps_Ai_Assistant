from openai import OpenAI
client = OpenAI()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot ended.Goodbye!")
        break

    prompt = "Answer in easy english but in 1 line only: " + user_input

    response = client.responses.create(
        model="gpt-4.1-mini", input=prompt, max_output_tokens=50
    )

    print("Assistant:", response.output_text)
