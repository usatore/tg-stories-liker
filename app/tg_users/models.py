from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class TGUsers(Base):
    __tablename__ = "tg_users"

    id = Column(Integer, primary_key=True, nullable=False)
    tg_id = Column(Integer, nullable=False)
    tg_nickname = Column(String, nullable=True)
    last_like_time = Column(DateTime, default=None)

