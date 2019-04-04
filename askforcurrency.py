from flask import Flask, render_template, request #imports, request

import requests

app = Flask("MyApp")


@app.route("/") #if they request smth
def serve_index():
    return render_template('currency.html') #expecting name variable; if you set it to none - print other thing, it is saved there

@app.route("/email", methods=["POST"]) #id like to have /signup, it can only submit info to us
def email():
    form_data = request.form #form we created in html
    print form_data["email"]

    requests.post(
    "https://api.mailgun.net/v3/sandbox052a2a89a39747a7b4fc06221bb3df89.mailgun.org/messages",
    auth=("api", "4c53fcbf3a7e92f818ea10ec64f84f5b-acb0b40c-8091e0ba"),
    data={"from": "Excited User <mailgun@sandbox052a2a89a39747a7b4fc06221bb3df89.mailgun.org>",
          "to": form_data["email"],
          "subject": "Hello",
          "text": "Hi! " + form_data ["name"] + " Testing some Mailgun awesomeness!"})
          #Hi {}, this is an emal".format(form_data["name"])


    return "Thank you"


app.run(debug=True)
