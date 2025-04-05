from fastapi import FastAPI
from app.telegram.tg_client import client
from app.telegram.tg_actions import process_user_stories
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await client.start()

    yield

    await client.disconnect()


app = FastAPI(lifespan=lifespan)





