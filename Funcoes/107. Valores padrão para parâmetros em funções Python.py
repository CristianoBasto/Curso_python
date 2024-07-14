  
'''
Valores padrao pra parametro de uma funçao:
Ao definir uma função, o parâmetro pode ter valores padrão(None). Caso o valor
enviado para o parâmetro, o valor padrão será usado.

'''

def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", "Total", x+y+z)
       
        
    else:
        print(f"{x=} {y=}", "Total", x+y)
       
        
soma(1,2,3)
soma(1,2)
soma(120, 90)
soma(x=10, z=30, y=2)