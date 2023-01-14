from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def root():
    return {'message': 'root'}


@app.get('/ksksksks')
def main():
    return {'message': 'meowWwWw...'}


@app.get('/db-task')
def main():
    return {'message': 'db task'}