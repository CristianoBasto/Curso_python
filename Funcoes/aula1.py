
soma=0
def Print(a, b, c=None):
 #  mult = (prim+segun)*mul
   if c is not None:
      print(f"{a=} {b=} {c=:.2f} total soma =", f"{a+b+c:.2f}")
   else:
    print(f"{a=} {b=} total soma =", f"{a+b:.2f}")

print("Primeiro numero")
a=int(input("Digite a:"))
b=int(input("Digite b:"))

print("Segundo numero")
c=int(input("Digite c:"))

Print(a,b)

print("2 exemplo")
Print(a,b,c)

