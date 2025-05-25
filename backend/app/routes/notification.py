from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.rabbitmq_service import publish_to_queue

router = APIRouter()

registered_tokens = set()

class TokenRequest(BaseModel):
    fcm_token: str

class NotificationRequest(BaseModel):
    title: str
    body: str
    data: dict
    image_url: str 
    action_url : str


@router.post("/devices/register")
async def register_device(token_request: TokenRequest):
    try:
        token = token_request.fcm_token
        if not token:
            raise HTTPException(status_code=400, detail="Token is required")

        registered_tokens.add(token)
        return {
            "message": "Token registered successfully",
            "total_registered": len(registered_tokens)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")



@router.post("/notifications/publish")
async def publish_notification(request: NotificationRequest):
    if not registered_tokens:
        return {"message": "No registered tokens"}

    try:
        for token in registered_tokens:
            publish_to_queue({
                "token": token,
                "title": request.title,
                "body": request.body,
                "data": request.data,
                "image_url": request.image_url,
                "action_url": request.action_url
            })
    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Failed to publish notification: {str(e)}")

    return {
        "message": "Notification tasks sent to RabbitMQ",
        "total": len(registered_tokens)
    }