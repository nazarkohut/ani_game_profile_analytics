from enum import Enum


class CustomEnum(Enum):
    def __str__(self) -> str:
        return self.name
