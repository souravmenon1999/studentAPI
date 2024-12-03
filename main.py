from fastapi import FastAPI
from controllers.student_controller import router as student_router
from dotenv import load_dotenv
import os
import logging
import uvicorn


load_dotenv()

# Fetch the PORT value
port = int(os.getenv("PORT", "8000"))
print(f"Port: {port}, Type: {type(port)}")

# Log setup
logging.basicConfig(level=logging.INFO)
logging.info(f"Starting FastAPI on port {port}")

app = FastAPI()
app.include_router(student_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="info")
