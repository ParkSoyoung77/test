from fastapi import FastAPI

# 1. 앱 인스턴스 생성
app = FastAPI()

# 2. 경로(Route) 설정
@app.get("/")
def home():
    return {"status": "success", "message": "FastAPI 세상에 오신 걸 환영합니다!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}