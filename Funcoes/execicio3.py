
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


multiplicar = criar_multiplicador(5)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(multiplicar(10))
print(triplicar(10))
print(quadruplicar(10))


def criar_multiplicador2(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

print("Numeros:")
duplicar1 = criar_multiplicador2(2)
triplicar1 = criar_multiplicador2(3)
quadruplicar2=criar_multiplicador2(4)

print(duplicar1(20))
print(triplicar1(20))
print(quadruplicar2(20))