from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.notification import router as notification_router
from app import globalExceptionHandler
from fastapi.exceptions import RequestValidationError

app = FastAPI()

app.add_exception_handler(RequestValidationError,globalExceptionHandler.validation_exception_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notification_router)

@app.get("/")
def root():
    return {"message": "Notification service is running"}