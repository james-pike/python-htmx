from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)

@app.get("/form1", response_class=HTMLResponse)
def form(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("form1.html", context)

@app.get("/progress", response_class=HTMLResponse)
def form(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("progress.html", context)


    