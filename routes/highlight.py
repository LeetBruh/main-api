from fastapi import APIRouter

from pydantic_models.highlight import CodeHighlightIn, CodeHighlightOut
from utils.highlight import highlight

router: APIRouter = APIRouter()


@router.post(
    path="/highlight",
    summary="Highlight",
    operation_id="highlight",
    description="Highlight code",
    response_model=CodeHighlightOut
)
async def highlight_code(
    highlight_in: CodeHighlightIn
) -> CodeHighlightOut:
    return highlight(highlight_in)
