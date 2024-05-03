from sqlalchemy import Column, Integer, String, select, update, ForeignKey, Boolean
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_session import SqlAlchemyBase as Base


class Submission(Base):
    __tablename__ = 'submissions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    challenge_id = Column(Integer, ForeignKey("challenges.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    code = Column(String, nullable=False)
    language = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=True)

    @classmethod
    async def get_all(cls, session: AsyncSession):
        _ = await session.execute(select(cls))
        return _.scalars().all()

    @classmethod
    async def get_by_challenge_id(cls, challenge_id: int, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.challenge_id == challenge_id))
        return _.scalars().all()

    @classmethod
    async def get_by_submission_id(cls, submission_id: int, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.id == submission_id))
        return _.scalar()

    @classmethod
    async def get_all_by_user_id(cls, user_id: int, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.id == user_id))
        return _.scalars().all()

    @classmethod
    async def get_all_by_user_id_and_challenge_id(cls, user_id: int, challenge_id: int, session: AsyncSession):
        _ = await session.execute(select(cls).where((cls.id == user_id) & (cls.challenge_id == challenge_id)))
        return _.scalars().all()
