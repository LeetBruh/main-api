from typing import List, Literal

from pydantic import BaseModel, ConfigDict


class ChallengeSample(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    explanation: str


class ChallengeInListItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    id: int
    title: str


class ChallengeFullOut(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    id: int
    title: str
    body: str
    samples: List[ChallengeSample]
    difficulty: Literal['easy', 'normal', 'hard']
