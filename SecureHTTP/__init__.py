import logging
from fastapi import FastAPI
import azure.functions as func
from routers import applicant
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Resume Parser API on Azure Functions")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(applicant.router)


def main(req: func.HttpRequest, context:func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.AsgiMiddleware(app).handle(req, context)