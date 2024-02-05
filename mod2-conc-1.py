# Agregação de Classes

class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salarioAnual(self):
        return (self.base*12) + self.bonus


class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salarioAgregado = salario

    def salarioTotal(self):
        return self.salarioAgregado.salarioAnual()


salario = Salario(10000, 700)
empregado = Empregado('Musachi', 46, salario) 

print(empregado.nome) # Output: Musachi
print(empregado.idade) # Output: 46
print(empregado.salarioTotal()) # Output: 120700