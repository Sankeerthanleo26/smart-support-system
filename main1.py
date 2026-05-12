from fastapi import FastAPI

# This 'app' variable is what the server looks for to start
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Project": "Smart Support System",
        "Status": "Sprint 1: Foundation",
        "Mode": "Development"
    }