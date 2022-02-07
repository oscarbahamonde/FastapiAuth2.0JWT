from uvicorn import run
from app import create_app
from dotenv import load_dotenv
from os import getenv

load_dotenv('app.env')

_app = create_app()

if '__main__' == __name__:
    run(_app,host=getenv('HOST'), port=getenv('PORT'))