from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount('/templates', StaticFiles(directory='templates'), name='templates')

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
def root(req: Request):
    return templates.TemplateResponse(name='index.html', context={'request': req})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)