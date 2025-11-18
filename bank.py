from branch import Branch

from typing import List

class Bank:
    def __init__(self, name: str, cnpj, address: str, phone: str):
        self.name = name
        self.cnpj = cnpj
        self.address = address  
        self.phone = phone
        self._branches: List['Branch'] = []