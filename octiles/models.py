from dataclasses import dataclass
from typing import Self


@dataclass
class DiffResult:
    removed: list
    new: list
    equals: dict
    unequals: dict

    @classmethod
    def create_empty(cls) -> Self:
        return cls(
            removed=[],
            new=[],
            equals={},
            unequals={}
        )
