from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义输入模型（用户可以看到的参数结构）
class AddInput(BaseModel):
    a: int
    b: int

# 定义输出模型（用户可以看到的返回值结构）
class AddOutput(BaseModel):
    result: int

# 隐藏的函数逻辑（部署后用户看不到）
def hidden_add(a: int, b: int) -> int:
    return a + b  # 这里可以是复杂逻辑，用户看不到

@app.post("/add", response_model=AddOutput)
def add_numbers(input: AddInput):
    result = hidden_add(input.a, input.b)
    return {"result": result}