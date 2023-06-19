import os
import app
import openai
import cosmoscmds
import json
from flask import Flask, redirect, render_template, request, url_for
import purconfig

app = Flask(__name__)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        output = user_input.upper()

       # response = openai.Completion.create(
       #     model="text-davinci-003",
       #     prompt=generate_prompt1(user_input),
       #     temperature=0.6,
       # )
       # output = url_for("index", result=response.choices[0].text)
       #json string data
        policy_string = '{"Action": "Deny", "operation": "Read", "classification": "Confidential", "user":"roshni@microsoft.com"}'

        #convert string to  object
        json_object = json.loads(policy_string)

        #check new data type
        print(type(json_object))

        return render_template('index.html', output=output, input=user_input, policy_object=json_object)
    return render_template('index.html')



def generate_prompt1(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

def generate_prompt_chat(animal):
    example_messages = [
        {
            "role": "system",
            "content": "You are a helpful, pattern-following assistant that translates corporate jargon into plain English.",
        },
        {
            "role": "system",
            "name": "example_user",
            "content": "New synergies will help drive top-line growth.",
        },
        {
            "role": "system",
            "name": "example_assistant",
            "content": "Things working well together will increase revenue.",
        },
        {
            "role": "system",
            "name": "example_user",
            "content": "Let's circle back when we have more bandwidth to touch base on opportunities for increased leverage.",
        },
        {
            "role": "system",
            "name": "example_assistant",
            "content": "Let's talk later when we're less busy about how to do better.",
        },
        {
            "role": "user",
            "content": "This late pivot means we don't have time to boil the ocean for the client deliverable.",
        },
    ]

def generate_embeddings(text):
    return openai.Embedding.create(
        input=text, model="text-embedding-ada-002"
    )["data"][0]["embedding"]

 #   len(embedding)

if __name__ == '__main__':
    app.run()



# Print response iteratively
#response = requests.get('<URL>')
#data = response.json()

#for key, value in data.items():
#    print(f'{key}: {value}')
