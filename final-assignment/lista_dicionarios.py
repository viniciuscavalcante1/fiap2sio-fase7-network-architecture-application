estudantes = [
    {"nome": "João", "notas": [70, 80, 90]},
    {"nome": "Maria", "notas": [85, 95, 100]},
    {"nome": "Pedro", "notas": [60, 65, 70]},
]

for estudante in estudantes:
    total = sum(estudante["notas"])
    media = total / len(estudante["notas"])
    if media > 80:
        print(estudante["nome"])
