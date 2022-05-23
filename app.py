import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
# pastresult = "\n\n NEXT"
fullresults = ["(responses are saved in order from newest to oldest entry)"]

@app.route("/", methods=("GET", "POST"))
def index():
    # pastresult = "\n\n NEXT"
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
  engine="text-curie-001",
  prompt=prompt + "\n",
  temperature=0.7,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0, 
)    
        # result=pastresult + prompt+": \n\n"
        # fullresult = redirect(url_for("index", result=response.choices[0].text + "\n"))
        
        # result = "\n\n"+prompt+": \n"+response.choices[0].text + fullresults[len(fullresults)-1]
        # add_pastresult(result)
        # result = "\n\n"+prompt+": \n"+response.choices[0].text
        # return render_template("index.html", result=result)


        return redirect(url_for("index", result="\n\n"+prompt+": \n"+response.choices[0].text))
    # result = request.args.get("result")+ return_pastresult()
    result = request.args.get("result")
    # add_pastresult(result)
    return render_template("index.html", result=result)

def add_pastresult(currentresult):
    fullresults.append(currentresult)

def return_pastresult():
    return ' '.join(fullresults)

