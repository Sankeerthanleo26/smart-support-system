from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Project": "Smart Support System",
        "Status": "Sprint 1: Foundation",
        "Mode": "Development"
    }
