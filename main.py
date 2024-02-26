from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount('/templates', StaticFiles(directory='templates'), name='templates')

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
def root(req: Request):
    return templates.TemplateResponse(name='/root/index.html', context={'request': req})


@app.get('/rooms', response_class=HTMLResponse)
def get_rooms(req: Request):
    return templates.TemplateResponse(name='/rooms/rooms.html', context={'request': req})


@app.get('/history', response_class=HTMLResponse)
def get_history(req: Request):
    return templates.TemplateResponse(name='history.html', context={'request': req})


@app.get('/spa', response_class=HTMLResponse)
def get_spa(req: Request):
    return templates.TemplateResponse(name='spa.html', context={'request': req})


@app.get('/gallery', response_class=HTMLResponse)
def get_gallery(req: Request):
    return templates.TemplateResponse(name='/gallery/gallery.html', context={'request': req})


@app.get('/restraunts', response_class=HTMLResponse)
def get_restraunts(req: Request):
    return templates.TemplateResponse(name='restraunts.html', context={'request': req})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=80, reload=True, reload_includes=['*.html', '*.css'])