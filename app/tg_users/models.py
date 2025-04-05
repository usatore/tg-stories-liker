from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, BigInteger

class TGUsers(Base):
    __tablename__ = "tg_users"

    id = Column(Integer, primary_key=True, nullable=False)
    tg_id = Column(BigInteger, nullable=False)
    tg_nickname = Column(String, nullable=True)
    last_like_time = Column(DateTime(timezone=True), default=None)

