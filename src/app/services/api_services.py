'''
Reads the Text File and Then Converts them into Currencies and Saves the File

'''

import json
import requests


def read_json_file(file_name: str) -> dict:
    '''
    Reading JSON File and returns the Converted Currency For Valid Entries

    '''

    with open(file_name, "r", encoding='UTF-8') as file:

        reader = json.loads(file.read())

        return reader


def currency_converter(input_value: int, input_currency: str, output_currency: str):
    '''
    This Function Validates the inputs and returns the converted currency
    '''
    url = 'https://api.exchangerate-api.com/v4/latest/'+input_currency

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    page = requests.get(url, headers=headers)

    load_dict = json.loads(page.text)

    if 'result' in load_dict:

        return {"value": input_value, "currency": 'input currency not supported'}

    price_dict = load_dict['rates']

    if not isinstance(input_value, (int, float)):

        return {"value": 'input value must be a numerical', "currency": input_currency}

    # nocheck for intput_value
    if output_currency in price_dict:

        value = input_value*price_dict[output_currency]

        return {"value": value, "currency": output_currency}

    return {"value": input_value, "currency": 'output currency not supported'}
