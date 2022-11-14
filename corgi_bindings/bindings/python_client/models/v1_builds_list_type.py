from enum import Enum


class V1BuildsListType(str, Enum):
    BREW = "BREW"
    KOJI = "KOJI"

    def __str__(self) -> str:
        return str(self.value)
