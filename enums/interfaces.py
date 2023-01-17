"""This file contains convenient interfaces/abstract classes
 that makes working with enums even more comfortable"""
from enum import Enum


class CustomEnum(Enum):
    """Implements methods that Enum class lack"""

    def __str__(self) -> str:
        """Helps to get string out of enum number"""
        return self.name.capitalize()

    @classmethod
    def get_enum_list(cls) -> list[any]:
        """::returns list of enum values defined inside enum class"""
        return list(map(lambda c: c.value, cls))

    @classmethod
    def get_enums_max_value(cls) -> any:
        """::returns maximum value from all possible enum values"""
        enum_values: list[any] = cls.get_enum_list()
        return max(enum_values)

    @classmethod
    def get_enums_min_value(cls) -> any:
        """::returns minimum value from all possible enum values"""
        enum_values: list[any] = cls.get_enum_list()
        return min(enum_values)
