from app.tg_users.models import TGUsers
from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
class TGUsersDAO(BaseDAO):
    model = TGUsers

    @classmethod
    async def get_tg_user_by_tg_id(cls, tg_id: int) -> TGUsers | None:
        async with async_session_maker() as session:
            result = await session.execute(
                select(cls.model).filter(cls.model.tg_id==tg_id)
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








