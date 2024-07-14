

def soma(*args):
    soma1=0
    for numero in args:
        soma1+=numero
    return soma1


m=soma(20,50,60,3,20,55,20)
print(m)