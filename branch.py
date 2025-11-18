from typing import List, TYPE_CHECKING
from bank import Bank

class Branch:
    def __init__(self, branch_id: str, address: str, phone: str, bank: 'Bank'):
        self.branch_id = branch_id
        self.address = address
        self.phone = phone
        self.bank = bank
        self._accounts: List['Account'] = []