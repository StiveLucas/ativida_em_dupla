from ABC import ABC
import os
os.system("clear")

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome: str = nome
        self.telefone: str = telefone
        self.email: float = email
        self.endereco: int = endereco

    def __str__(self) -> str:
        return f"\nFuncionario: \nNome: {self.nome} \nTelefone: {self.telefone} \nE-mail: {self.email} \nEndereço: {self.endereco}"