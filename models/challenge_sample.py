from sqlalchemy import Column, Integer, String, select, update, ForeignKey, event
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_session import SqlAlchemyBase as Base


class ChallengeSample(Base):
    __tablename__ = 'samples'
    id = Column(Integer, primary_key=True, autoincrement=True)
    challenge_id = Column(Integer, ForeignKey("challenges.id"))
    explanation = Column(String, nullable=False)

    @classmethod
    async def get_all(cls, session: AsyncSession):
        _ = await session.execute(select(cls))
        return _.scalars().all()

    @classmethod
    async def get_by_challenge_id(cls, challenge_id: int, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.challenge_id == challenge_id))
        return _.scalar()

    @classmethod
    async def get_by_sample_id(cls, sample_id: int, session: AsyncSession):
        _ = await session.execute(select(cls).where(cls.id == sample_id))
        return _.scalar()


def insert_sample_data(target, connection, **kwargs):
    connection.execute(
        target.insert(),
        {
            'id': 1,
            'challenge_id': 1,
            'explanation': """
            Input: x = 4
            Output: 2
            Explanation: The square root of 4 is 2, so we return 2.
            """
        },
        {
            'id': 2,
            'challenge_id': 1,
            'explanation': """
            Input: x = 8
            Output: 2
            Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
            """
        }
    )


event.listen(ChallengeSample.__table__, 'after_create', insert_sample_data)