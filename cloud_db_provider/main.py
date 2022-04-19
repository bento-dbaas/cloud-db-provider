from fastapi import FastAPI

app = FastAPI()

@app.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}


@app.get("/oi", status_code=200)
async def oi():
    return {"message": "Oi"}

@app.get("/healthcheck", status_code=200)
async def healthcheck():
    return {"message": "SUCCESS"}
