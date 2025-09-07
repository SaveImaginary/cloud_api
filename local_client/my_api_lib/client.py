import requests
from pydantic import BaseModel

API_URL = "http://cloud-api.zeabur.app/"

class AddInput(BaseModel):
    a: int
    b: int

class AddOutput(BaseModel):
    result: int

def add(a: int, b: int) -> int:
    input_data = AddInput(a=a, b=b)
    response = requests.post(API_URL, json=input_data.dict())
    if response.status_code == 200:
        output = AddOutput(**response.json())
        return output.result
    else:
        raise Exception(f"API error: {response.text}")