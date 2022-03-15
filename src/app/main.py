"""
Main Script for running the FastAPI Server for Currency Converter Service

"""

import logging

from fastapi import FastAPI

from app.controllers import api_controller

log = logging.getLogger("Currency_Converter_Service")


def create_application() -> FastAPI:
    """
    Starts the Fast API Server and Includes the Endpoint in the routes"

    """
    log.info("Starting up...")

    fastapi_app = FastAPI()

    fastapi_app.include_router(api_controller.router,
                       tags=["summaries"]
                       )

    return fastapi_app


app = create_application()


@app.on_event("startup")
async def startup_event():
    """
    logs the startup
    """
    log.info("Starting up...")
    log.info('Currency Converter Service')


@app.on_event("shutdown")
async def shutdown_event():
    """
    logs the shutdown
    """
    log.info("Shutting down...")
