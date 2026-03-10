from fastapi import FastAPI , Form , Request , Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

app = FastAPI()
app.mount("/public" , StaticFiles(directory=str(BASE_DIR/"public")) , name="public")


def get_prime_factors(inp):
    numbers = []


    while inp%2 == 0:   # excluded 2
        numbers.append(2)
        inp//=2
    
    while inp%3 == 0:   # excluded 3
        numbers.append(3)
        inp//=3

    i = 5
    while i*i <=inp:     # excluded i^2
        while inp%i == 0: # excluded non divisible
            numbers.append(i)
            inp //=i
        i+=2             # excluded even

    if (inp > 1):
        numbers.append(inp)
    return numbers

@app.get("/" , response_class=HTMLResponse)
def Home(request : Request):
    return templates.TemplateResponse(
        "index.html" , 
        {"request" : request}
    )


@app.post("/calc" , response_class=HTMLResponse )
def calc(request: Request , user_input: int = Form()):
    result = get_prime_factors(user_input)
    return templates.TemplateResponse(
        "index.html", 
        {
            "request" : request , 
            "result" : result
        }
    )


@app.get("/" , response_class=HTMLResponse)
def About(request : Request):
    return templates.TemplateResponse(
        "about.html" , 
        {"request" : request}
    )
