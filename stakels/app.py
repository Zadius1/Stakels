import uuid
from dataclasses import dataclass, field
from typing import Dict, Optional, List

@dataclass
class User:
    username: str
    balance: float = 0.0

@dataclass
class Bet:
    description: str
    amount: float
    creator: str
    opponent: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    winner: Optional[str] = None

class BetManager:
    def __init__(self):
        self.bets: Dict[str, Bet] = {}
        self.users: Dict[str, User] = {}

    def create_user(self, username: str) -> User:
        if username in self.users:
            return self.users[username]
        user = User(username=username)
        self.users[username] = user
        return user

    def create_bet(self, description: str, amount: float, creator: str, opponent: str) -> Bet:
        if creator not in self.users or opponent not in self.users:
            raise ValueError("Both creator and opponent must be registered users")
        bet = Bet(description=description, amount=amount, creator=creator, opponent=opponent)
        self.bets[bet.id] = bet
        return bet

    def list_bets(self) -> List[Bet]:
        return list(self.bets.values())
