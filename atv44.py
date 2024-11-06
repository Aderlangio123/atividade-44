windowsXP = []  # 1
Unix = []       # 2
Linux = []      # 3
Netware = []    # 4
MacOS = []      # 5
outros = []     # 6

votos = []

def calculo_porcentagem(lista_votos, total_votos):
    return (len(lista_votos) / total_votos) * 100 if total_votos > 0 else 0


while True:
    print("""
        windowsXP =  # 1
        Unix =  # 2
        Linux =   # 3
        Netware =  # 4
        MacOS =    # 5
        outros =  # 6""")
    op = int(input("Digite a sua opinião sobre qual o melhor sistema operacional segundo a tabela informada!  (0 para parar): "))
    if op < 0 or op > 6:
        print("Digite um voto válido de acordo com a tabela!")
    elif op == 0:
        break
    votos.append(op)


for item in votos:
    if item == 1:
        windowsXP.append(item)
    elif item == 2:
        Unix.append(item)
    elif item == 3:
        Linux.append(item)
    elif item == 4:
        Netware.append(item)
    elif item == 5:
        MacOS.append(item)
    elif item == 6:
        outros.append(item)

total_votos = len(votos)
print(" ")
print("SISTEMAS OPERACIONAIS - VOTOS: ")
print(" ")

r1 = calculo_porcentagem(windowsXP, total_votos)
print(f" Windows XP é: {r1} %")

r2 = calculo_porcentagem(Unix, total_votos)
print(f" Unix é: {r2} %")

r3 = calculo_porcentagem(Linux, total_votos)
print(f" Linux é: {r3} %")

r4 = calculo_porcentagem(Netware, total_votos)
print(f" Netware é: {r4} %")

r5 = calculo_porcentagem(MacOS, total_votos)
print(f" MacOS é: {r5} %")

r6 = calculo_porcentagem(outros, total_votos)
print(f" Outros é: {r6} %")