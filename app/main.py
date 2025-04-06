from contextlib import asynccontextmanager
from app.scheduler import start_scheduler

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.router import router
from app.telegram.tg_actions import process_user_stories
from app.telegram.tg_client import client


@asynccontextmanager
async def lifespan(app: FastAPI):
    await client.start()

    start_scheduler()

    yield

    await client.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(router)

"""app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)"""
