"""Contains custom types and dataclasses for various methods/functions"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class DeltaDatesGeneration:
    """Type that specifies parameters for methods like generate_days_with_specified_deltas"""
    date: datetime.date
    number_of_dates: int
    reverse: bool = False
    delta_years: int = 0
    delta_months: int = 0
    delta_days: int = 0
