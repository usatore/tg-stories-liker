from fastapi import FastAPI
from app.telegram.tg_client import client
from app.telegram.tg_actions import process_user_stories
from contextlib import asynccontextmanager
from app.router import router
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await client.start()

    yield

    await client.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






