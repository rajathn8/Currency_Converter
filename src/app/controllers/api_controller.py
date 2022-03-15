"""
Main File to Add Routes to the Currency Converter Service
Todo
1 - Add More Endpoints
2 - Include HTTP Exceptions
3 - Include Response Model

"""

from fastapi import APIRouter, Depends
from app.models import api_models
from app.services import api_services


router = APIRouter()


@router.get('/',
            description='Rajath Rao - Currency Converter Service',
            status_code=200)
def base_url():
    """
    Test endpoint
    go to -> /info
    """
    return {"Stylight": "Currency Converter Service"}


@router.get('/info',
            description='Returns the Information of the Application such as Name and environment',
            response_model=api_models.InfoModel,
            status_code=200)
def color_suggestor_info():
    """
    Test endpoint
    go to -> /info

    Returns Information about the Service
    """
    return api_models.InfoModel()


@router.get("/convert/",
            description='Returns the Information of the Application such as Name and environment',
            status_code=200)
async def convert_currency(params: api_models.InputCurrency = Depends()):
    """
    endpoint
    go to -> /convert/

    Convert Currency Based on Input
    """
    value = api_services.currency_converter(
        params.input_value, params.input_currency, params.output_currency)
    return value
