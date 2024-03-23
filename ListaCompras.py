lista_compras = []

while True:
    producto = input("Ingrese el nombre del producto (o 'terminar' para finalizar): ")
    if producto == "terminar":
        break
    else:
        lista_compras.append(producto)

print("Lista de compras:")
for producto in lista_compras:
    print(producto)
