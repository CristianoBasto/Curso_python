'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atigir..
Existe o escopo global e local.
 * O escopo global é o escopo onde todo o código é alcançável.
 * O escopo local é o escopo onde apenas nomes do mesmo local
 podem ser alçancados.
'''


#  Escopo global.
x=0


def escopo():
    # Escopo local.
    x = 1
    print(x)
    x=11
x = 10
escopo()