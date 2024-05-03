from sqlalchemy import Column, Integer, String, select, event
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship

from models.db_session import SqlAlchemyBase as Base


class Challenge(Base):
    __tablename__ = 'challenges'
    id = Column(Integer, primary_key=True, autoincrement=True)
    samples = relationship("ChallengeSample", lazy="selectin")
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)

    @classmethod
    async def get_all(cls, session: AsyncSession):
        _ = await session.execute(select(cls))
        return _.scalars().all()

    @classmethod
    async def get_by_challenge_id(cls, challenge_id: int, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.id == challenge_id))
        return _.scalar()


def insert_sample_data(target, connection, **kwargs):
    connection.execute(
        target.insert(),
        {
            'id': 1,
            'title': 'Sqrt(x)',
            'difficulty': 'easy',
            'body': """
            Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
            The returned integer should be non-negative as well.

            You must not use any built-in exponent function or operator.

            For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
            """
        }
    )


event.listen(Challenge.__table__, 'after_create', insert_sample_data)
