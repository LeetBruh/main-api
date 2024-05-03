from pydantic import BaseModel, ConfigDict


class SubmissionIn(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    code: str
    language: str
    challenge_id: int


class SubmissionInListItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    id: int
    language: str
    challenge_id: int
    code: str


class SubmissionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    submission_id: int
