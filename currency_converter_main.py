'''
Reads the Text File and Then Converts them into Currencies and Saves the File

'''
import argparse
from src.app.services.api_services import read_json_file, currency_converter


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Return Currency Converted JSON File')
    parser.add_argument('-f', '--filename', help='File to be Parsed')
    parser.add_argument(
        '-t', '--target_currency', help='Target Currency')

    args = parser.parse_args()

    input_file = read_json_file(args.filename)
    target_currency = args.target_currency

    for request_values in input_file:
        print(currency_converter(
            request_values["value"], request_values["currency"], target_currency))
