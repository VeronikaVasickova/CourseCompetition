from flask import Flask, render_template, request, send_from_directory #imports, request
import requests
import os
from decimal import *

from forex_python.converter import CurrencyRates


app = Flask("MyApp", static_folder='templates')
result = 0
c = CurrencyRates(force_decimal=False)
selected_currency = ""
desired_currency = ""
amount=0


@app.route("/")
def Convert():
    return render_template("currency.html")

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists("templates/" + path):
        return send_from_directory("templates/", path)
    else:
        return send_from_directory("build", "expenditure.html")

@app.route("/converter", methods=["POST"])
def GetCurrency():
    form_data = request.form #form we created in html
    selected_currency = form_data["Available_Currencies"] #html available currencies drop down menu
    amount = form_data["amount"]
    desired_currency = form_data["Desired_Currencies"]

    amount.join(map(str,amount))
    a=Decimal(amount)
    convertion_rate = c.get_rate(selected_currency, desired_currency)
    res = Decimal(convertion_rate)*a
    res = round(res, 2)
    return render_template("expenditure.html", result = res )

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
















    # my currency select; enter amount of money; select to which cucrency
    # submit button connected with html
    # forex-python
