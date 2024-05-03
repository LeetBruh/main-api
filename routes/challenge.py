from typing import List

from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from models.challenge import Challenge
from models.db_session import get_session
from pydantic_models.challenge import ChallengeInListItemOut, ChallengeFullOut

router = APIRouter()


@router.get(
    path="/all",
    summary="Challenges",
    operation_id="challenges",
    description="Get all challenges",
    response_model=List[ChallengeInListItemOut]
)
async def get_all_challenges(
    session: AsyncSession = Depends(get_session)
) -> List[ChallengeInListItemOut]:
    challenges = await Challenge.get_all(session)
    return [ChallengeInListItemOut.model_validate(challenge) for challenge in challenges]


@router.get(
    path="/id/{challenge_id}",
    summary="Get challenge by id",
    operation_id="challenge-by-id",
    description="Get challenge by challenge ID",
    response_model=ChallengeFullOut
)
async def get_challenge_by_id(
    challenge_id: int,
    session: AsyncSession = Depends(get_session)
) -> ChallengeFullOut | Response:
    if challenge := await Challenge.get_by_challenge_id(challenge_id, session):
        return ChallengeFullOut.model_validate(challenge)
    return Response(status_code=404)
