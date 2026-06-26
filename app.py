from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    user_question = ""
    ai_answer = ""

    if request.method == "POST":

        user_question = request.form["question"]

        prompt = "Answer in easy english but in 1 line only: " + user_question

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            max_output_tokens=50
        )

        ai_answer = response.output_text

    return render_template(
        "index.html",
        question=user_question,
        answer=ai_answer
    )

if __name__ == "__main__":
    app.run(debug=True)
