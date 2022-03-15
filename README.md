# Currency_Converter CLI

 Implement CLI to convert currencies

# Usage

Run the command below in the source directory

```python3 currency_converter_main.py --filename  [filename] --target_currency [target_currency]```

to save the output to a text file

```python3 currency_converter_main.py --filename  [filename] --target_currency [target_currency] &>output.txt```



# Currency_Converter API

Implement an API to convert currencies -https://tinyurl.com/rajathcurrencyconverter

# Instructions on how to build and run the app

# Usage

Run the command below in the source/app directory

```uvicorn main:app ``` or ```uvicorn main:app --reload```

go to  ```http://127.0.0.1:8000/docs``` to check the endpoints

# Endpoints

# Info Endpoint

Returns the Information of the Alexa Service
```
/info --> {
            "app_name": "Currency Converter API Services",
            "env_name": "Scraping Services",
            "version": 2,
            "description": "Currency Converter Converts Currency"
        }
```

### Converter Value

``` /converter/ ```  - Converts a Currency to an another Currency

```
Input

    input_value: int
    input_currency: str
    output_currency: str

```

```
Output
    
    output_value: int
    output_currency: str

```
# Testing

         Navigate to the Source Folder and Run

```python3 -m pytest tests```
