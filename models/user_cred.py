from sqlalchemy import Column, Integer, String, select, update, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_session import SqlAlchemyBase as Base


class UserCred(Base):
    __tablename__ = 'user_creds'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    @classmethod
    async def get_by_login(cls, login: str, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.login == login))
        return _.scalar()

    @classmethod
    async def get_by_user_id(cls, user_id: int, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.user_id == user_id))
        return _.scalar()

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()
