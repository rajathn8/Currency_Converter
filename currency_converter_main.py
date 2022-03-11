'''
Approach 1
Using List and Dict

Reads the Text File and Then Converts them into Currencies and Saves the File

'''
import argparse
import json
import sys

STATIC_PRICE_FILE = "current_values.json"


def read_json_file(file_name):
    '''
    Reading JSON File and returns the Converted Currency For Valid Entries

    '''

    with open(file_name, "r", encoding='UTF-8') as file:

        reader = json.loads(file.read())

        return reader


def main_currency_converter_function(input_value, output_currency, price_dict):
    '''
    This Function Validates the inputs and returns the converted currency
    '''

    if (input_value["currency"] in price_dict) and not isinstance(input_value['value'], str):

        return static_currency_converter(input_value, output_currency, price_dict)

    else:
        # Input is Invalid
        #print(type(input_value['value']),input_value['value'])
        return {"value": 0, "currency": output_currency}


def static_currency_converter(input_value, currency, price_dict):
    '''
    This Function Takes in the Input Value 
    and the Currency Type and Returns the 
    Coverted Currency
    '''

    # First Step
    # Convert Value to Euro's
    
    if input_value['currency'] == currency:
        return {"value": input_value['value'], "currency": currency}
    
    else:
        
        price_in_euro = input_value["value"]/price_dict[input_value['currency']]
        
        value = price_in_euro * price_dict[currency]
        
        return {"value": value, "currency": currency}


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Return Currency Converted JSON File')
    parser.add_argument('-f', '--filename', help='File to be Parsed')
    parser.add_argument(
        '-t', '--target_currency', help='Target Currency')

    args = parser.parse_args()

    input_file = read_json_file(args.filename)
    target_currency = args.target_currency

    price_dict = read_json_file(STATIC_PRICE_FILE)[0]
    

    for request_values in input_file:
        print(main_currency_converter_function(
            request_values, target_currency, price_dict))
