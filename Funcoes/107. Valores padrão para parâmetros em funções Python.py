  
'''
Valores padrao pra parametro de uma funçao:
Ao definir uma função, o parâmetro pode ter valores padrão(None). Caso o valor
enviado para o parâmetro, o valor padrão será usado.

'''

def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", "Total", x+y+z)
        print(f"Parâmetro Padrão \n")
        
    else:
        print(f"{x=} {y=}", "Total", x+y)
        print("Parâmetro enviado")
        
        


soma(1,2,3)
soma(1,2)