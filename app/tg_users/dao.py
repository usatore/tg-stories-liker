from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.tg_users.models import TGUsers


class TGUsersDAO:
    model = TGUsers

    @classmethod
    async def get_tg_user_by_tg_id(cls, tg_id: int) -> TGUsers | None:
        async with async_session_maker() as session:
            result = await session.execute(
                select(cls.model).filter(cls.model.tg_id == tg_id)
            )
            tg_user = result.scalars().first()
            return tg_user

    @classmethod
    async def add_tg_user(cls, tg_id: int, tg_nickname: str):
        new_user = cls.model(tg_id=tg_id, tg_nickname=tg_nickname)

        try:
            async with async_session_maker() as session:
                session.add(new_user)
                await session.commit()
                return new_user

        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                print("Database Exc")
            elif isinstance(e, Exception):
                print("Unknown Exc")

    @classmethod
    async def update_last_like_time(cls, tg_id: int):

        async with async_session_maker() as session:

            result = await session.execute(
                select(cls.model).filter(cls.model.tg_id == tg_id)
            )
            tg_user = result.scalars().first()

            if tg_user:
                tg_user.last_like_time = datetime.now(tz=timezone.utc)

                await session.commit()
