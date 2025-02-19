from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data":{'name':'kavin'}}

@app.get('/about')
def about():
    return {'data':{'about page'}}

@app.get('/blog/{id}')
def blog(id):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    data = {1:20, 100:30}
    return data[id]