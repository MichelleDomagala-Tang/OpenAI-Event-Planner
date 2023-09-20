'''
Developed with the help of OpenAI Documentation https://platform.openai.com/docs/introduction
'''

import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

'''
Make POST request to the OpenAI API and render the results
'''
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        input = request.form["input"]
        # Sends the API Request
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=input,
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

'''
A function that formats user input to be clear and concise to be sent to the OpenAI API
'''
def generate_prompt(input):
    # Todo: Format input, create input boxes (event type, dates etc) then format into a prompt
    return input
