import requests, json
from datetime import datetime

def exchange_func():
    try:
        with open('JSON_data.json', 'r', encoding="utf-8") as file:
            string = file.read()

        JSON = json.loads(string)
        if datetime.date(datetime.today()) == JSON['date']:
            JSON_valuts = JSON['rates']
            return JSON_valuts
        else:
            url = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD,EUR,UAH,HUF,TRY,PLN,SEK,KZT,BYN,GBP&base=CZK"
            payload = {}
            headers = {
                "apikey": "3b6HDfQq2rQfYeWAU5lPBq03SR9jYlP9"
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            status_code = response.status_code
            result = response.text
            JSON = json.loads(result)
            JSON_valuts = JSON['rates']
            with open('JSON_data.json', 'w', encoding="utf-8") as file:
                print(JSON, file=file)
            return JSON_valuts

    except:
        url = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD,EUR,UAH,HUF,TRY,PLN,SEK,KZT,BYN,GBP&base=CZK"
        payload = {}
        headers = {
            "apikey": "3b6HDfQq2rQfYeWAU5lPBq03SR9jYlP9"
        }
        response = requests.request("GET", url, headers=headers, data = payload)
        status_code = response.status_code
        result = response.text
        JSON = json.loads(result)
        JSON_valuts = JSON['rates']
        with open('JSON_data.json', 'w', encoding="utf-8") as file:
            print(JSON, file=file)
        return JSON_valuts


# JSON_valuts = exchange()['rates']
# def exchange(JSON : dict = None):
#     if JSON is None:
#         url = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD,EUR,UAH,HUF,TRY,PLN,SEK,KZT,BYN,GBP&base=CZK"
#         payload = {}
#         headers = {
#             "apikey": "3b6HDfQq2rQfYeWAU5lPBq03SR9jYlP9"
#         }
#         response = requests.request("GET", url, headers=headers, data=payload)
#         status_code = response.status_code
#         result = response.text
#         JSON = json.loads(result)
#     if datetime.date(datetime.today()) == JSON['date']:
#         JSON_valuts = JSON['rates']
#         return JSON_valuts
#     else:
#         url = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD,EUR,UAH,HUF,TRY,PLN,SEK,KZT,BYN,GBP&base=CZK"
#
#         payload = {}
#         headers = {
#             "apikey": "3b6HDfQq2rQfYeWAU5lPBq03SR9jYlP9"
#         }
#
#         response = requests.request("GET", url, headers=headers, data = payload)
#
#         status_code = response.status_code
#         result = response.text
#
#         JSON = json.loads(result)
#         JSON_valuts = JSON['rates']
#         return JSON_valuts
#     # JSON_date = JSON['date']
#
# JSON = exchange()