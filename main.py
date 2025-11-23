from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class CalculationRequest(BaseModel):
    a: float
    b: float


class CalculationResponse(BaseModel):
    result: float


@app.get("/")
def root():
    return {"message": "Calculator API"}


@app.post("/add", response_model=CalculationResponse)
def add(request: CalculationRequest):
    return CalculationResponse(result=request.a + request.b)


@app.post("/subtract", response_model=CalculationResponse)
def subtract(request: CalculationRequest):
    return CalculationResponse(result=request.a - request.b)


@app.post("/multiply", response_model=CalculationResponse)
def multiply(request: CalculationRequest):
    return CalculationResponse(result=request.a * request.b)


@app.post("/divide", response_model=CalculationResponse)
def divide(request: CalculationRequest):
    if request.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return CalculationResponse(result=request.a / request.b)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
