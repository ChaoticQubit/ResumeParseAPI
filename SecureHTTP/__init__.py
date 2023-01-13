import logging, utils
from fastapi import FastAPI
import azure.functions as func
from routers import applicant
from schemas import schemaMain as schemas

app = FastAPI()
app.include_router(applicant.router)

def main(req: func.HttpRequest, context:func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.AsgiMiddleware(app).handle(req, context)