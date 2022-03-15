"""
Models for Currency Converter API
"""
from pydantic import BaseModel


class InfoModel(BaseModel):
    """
    Info Endpoint Response Model
    """
    app_name: str = "Currency Converter API Services"
    env_name: str = "Scraping Services"
    version: int = 2
    description: str = "Currency Converter Converts Currency"


class InputCurrency(BaseModel):
    """
    Input Base Model
    """
    input_value: int
    input_currency: str
    output_currency: str
