from typing import Literal, List

from pydantic import BaseModel, ConfigDict


class CodeHighlightIn(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    code: str
    language: str


class ColorizedToken(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    text_color: Literal['unspecified', 'first', 'second', 'third', 'fourth', 'fifth']
    text_appearance: Literal['normal', 'italic', 'crossed_out']
    text: str
    start_index: int
    end_index: int


class CodeHighlightOut(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    tokens: List[ColorizedToken]
