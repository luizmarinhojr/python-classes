# Método de classe X Método Estático

from datetime import date

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método de Classe -> Retorna a idade a partir do ano de nascimento
    # Ano atual - Ano Nascimento = idade
    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    
    # Método Estático -> Verifica se é maior de idade
    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18
    

pessoa1 = Pessoa('Maria', 26)
pessoa2 = Pessoa.apartirAnoNascimento('Ana', 2006)

# Imprimir o resultado
print(pessoa1.idade) # Output: 26
print(pessoa2.idade) # Output: 18
print(Pessoa.ehMaiorIdade(17))  # Output: False