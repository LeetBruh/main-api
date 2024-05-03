import re
from typing import List

from pydantic_models.highlight import CodeHighlightIn, ColorizedToken, CodeHighlightOut


def highlight(highlight_in: CodeHighlightIn) -> CodeHighlightOut:
    keywords = ['fun', 'val', 'var', 'if', 'else', 'for', 'while', 'return', 'class', 'interface', 'object', 'when']
    tokens: List[ColorizedToken] = []
    for keyword in keywords:
        for match in re.finditer(r'\b' + keyword + r'\b', highlight_in.code):
            token = ColorizedToken(
                text_color='second',
                text_appearance='normal',
                text=match.group(),
                start_index=match.start(),
                end_index=match.end()
            )
            tokens.append(token)
    return CodeHighlightOut(tokens=tokens)
