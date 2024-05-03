from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth_bearer import JWTBearer, JWTHeader
from models import Submission
from models.db_session import get_session
from pydantic_models.submission import SubmissionInListItemOut, SubmissionIn, SubmissionOut

router: APIRouter = APIRouter()


@router.get(
    path="/all",
    summary="Submissions of current user",
    operation_id="submissions",
    dependencies=[Depends(JWTBearer())],
    description="Get all submissions",
    response_model=List[SubmissionInListItemOut]
)
async def get_all_submissions(
    token: JWTHeader = Depends(JWTBearer()),
    session: AsyncSession = Depends(get_session)
) -> List[SubmissionInListItemOut]:
    submissions = await Submission.get_all_by_user_id(token.user_id, session)
    return [SubmissionInListItemOut.model_validate(submission) for submission in submissions]


@router.get(
    path="/all/{challenge_id}",
    summary="Submissions of current user by challenge",
    operation_id="submissions-by-challenge-id",
    dependencies=[Depends(JWTBearer())],
    description="Get all submissions",
    response_model=List[SubmissionInListItemOut]
)
async def get_all_submissions(
    challenge_id: int,
    token: JWTHeader = Depends(JWTBearer()),
    session: AsyncSession = Depends(get_session)
) -> List[SubmissionInListItemOut]:
    submissions = await Submission.get_all_by_user_id_and_challenge_id(token.user_id, challenge_id, session)
    return [SubmissionInListItemOut.model_validate(submission) for submission in submissions]


@router.put(
    path="/make",
    summary="Make submission in challenge",
    operation_id="make-submission",
    dependencies=[Depends(JWTBearer())],
    description="Make submission",
    response_model=SubmissionOut
)
async def make_submission(
    request: SubmissionIn,
    token: JWTHeader = Depends(JWTBearer()),
    session: AsyncSession = Depends(get_session)
) -> SubmissionOut:
    submission = Submission(**request.model_dump())
    submission.user_id = token.user_id
    session.add(submission)
    await session.commit()
    return SubmissionOut.model_validate(SubmissionOut(submission_id=submission.id))
