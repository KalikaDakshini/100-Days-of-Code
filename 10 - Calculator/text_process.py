"""Functions to process text."""

import re
from typing import NamedTuple

token_spec = [
    ("NUMBER", r"[+\-]?\d+(?:\.\d+)?"),
    ("OPCODE", r"[+\-*/]"),
    ("PAREN", r"[()]"),
]

RGX_EXPR = "|".join(
    [f"(?P<{name}>{pattern})" for (name, pattern) in token_spec]
)
tkn_regex = re.compile(RGX_EXPR)


class Token(NamedTuple):
    """Represents elements of arithmetic expression."""

    type: str | None
    value: str

    def __str__(self) -> str:
        return f"{self.type}: {self.value}"


def tokenize(arith_expr: str) -> list[Token]:
    """Convert expression string to a list of Token."""
    tkn_list = []
    for match_obj in tkn_regex.finditer(arith_expr):
        tkn_list.append(Token(match_obj.lastgroup, match_obj.group()))

    return tkn_list
