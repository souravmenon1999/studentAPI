from fastapi import FastAPI
from controllers.student_controller import router as student_router

app = FastAPI()

app.include_router(student_router)

# Run the app with: uvicorn main:app --reload
