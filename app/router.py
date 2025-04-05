from fastapi import APIRouter
from app.telegram.tg_actions import process_user_stories
from app.telegram.tg_client import client



router = APIRouter(
    tags=['Сервис'],
)


@router.post("/like_stories")
async def like_stories():
    try:
        await process_user_stories(client)
    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
