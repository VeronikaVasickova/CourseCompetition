from flask import Flask, render_template, request #imports, request
import requests

from forex_python.converter import CurrencyRates
    c = CurrencyRates()
    app = Flask("MyApp")

    selected_currency
    desired_currency
    amount

currencies = [
    'USD', 'BGN', 'CZK', 'GBP', 'CNY', 'EUR']

@app.route('/')


@app.route("/converter", methods=["POST"])
def GetCurrency():
    form_data = request.form #form we created in html
    selected_currency = form_data["Available_Currencies"] #html available currencies drop down menu
    amount = form_data["amount"]
    desired_currency = form_data["Desired_Currencies"]

    convertion_rate = c.get_rate(selected_currency, desired_currency)
    result=convertion_rate*amount

return render_template('currency.html',result=result.title())

















    # my currency select; enter amount of money; select to which cucrency
    # submit button connected with html
    # forex-python
