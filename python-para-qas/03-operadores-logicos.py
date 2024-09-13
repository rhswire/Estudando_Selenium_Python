a = 10
b = 25
c = 30

# and

if a < b and b < c:
    print("ambas as condições são verdadeiras")
else:
    print("uma ou ambas as condições são falsas")

# or

if a < b or b < c:
    print("pelo menos uma das condições é verdadeira")
else:
    print("nenhuma das condições é verdadeira")

# not (inverte o resultado do que está ali)

if not a < b:
    print("a é maior ou igual a b")
else:
    print("a é menor que b")

verdadeiro = True
print(not(verdadeiro))