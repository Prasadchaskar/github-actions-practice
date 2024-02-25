from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hi Prasad"}

# route to reverse string
@app.get("/{random_string}")
async def return_reverse_str(random_string:str):
    return "".join(reversed(random_string))