tupla = (1, 2, 3, 4, 5)
try:
    tupla.append(6)
except AttributeError as e:
    print("Erro: " + str(e))