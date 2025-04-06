from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.scheduler import start_scheduler
from app.telegram.tg_client import client


@asynccontextmanager
async def lifespan(app: FastAPI):

    await client.start()

    start_scheduler()

    yield

    await client.disconnect()


app = FastAPI(lifespan=lifespan)
