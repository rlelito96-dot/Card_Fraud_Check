from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TransactionStatus(str, Enum):
    APPROVED = "APPROVED"
    REVIEW = "REVIEW"
    BLOCKED = "BLOCKED"


@dataclass
class Transaction:
    """Class for representing financial transaction.
    - timestamp: transaction execution time
    """

    id: str
    user_id: str
    amount: float
    country: str
    timestamp: datetime
