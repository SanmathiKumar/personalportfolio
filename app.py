from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Define routes for the home page, projects page, and contact page
# Each route renders the corresponding HTML template using Jinja2Templates
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# The "/projects" route renders the "projects.html" template, and the "/contact" route renders the "contact.html" template.
@app.get("/projects", response_class=HTMLResponse)
def read_projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})
