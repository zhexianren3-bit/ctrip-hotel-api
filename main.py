from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "携程酒店API"}
@app.get("/hotels")
def hotels(city: str = "北京"):
    return {"success": True, "hotels": [{"name": "酒店1", "price": 500}]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
