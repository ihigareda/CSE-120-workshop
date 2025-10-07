from fastapi import FastAPI

app = FastAPI(title="CSE120 GitHub Workshop")

@app.get("/health") 
async def health_check() -> dict[str, str]:
    return {"status": "ok"}