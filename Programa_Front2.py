print ('Hello world!')

# Marconi_Aragão

# Desenvolva um programa que: 

# colete dados da altura e o gênero (Masculino ou Feminino) de 15 pessoas e apresente os seguintes resultados:
# A maior e a menor altura do grupo;
# A média de altura das pessoas do gênero Masculino;
# O número de pessoas do gênero Feminino.

alturas = []
generos = []

for i in range(15):
    while True:
        try:
            altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
            if altura <= 0:
                print("Altura deve ser positiva.")
                continue
            break
        except ValueError:
            print("Digite um valor válido para altura.")
    while True:
        genero = input(f"Digite o gênero da pessoa {i+1} (M para Masculino, F para Feminino): ").strip().upper()
        if genero in ['M', 'F']:
            break
        else:
            print("Digite apenas 'M' ou 'F'.")
    alturas.append(altura)
    generos.append(genero)

maior_altura = max(alturas)
menor_altura = min(alturas)

# Média de altura dos homens

alturas_masculino = [alturas[i] for i in range(15) if generos[i] == 'M']
media_masculino = sum(alturas_masculino) / len(alturas_masculino) if alturas_masculino else 0

# Número de mulheres

num_feminino = generos.count('F')

print(f"A maior altura do grupo é: {maior_altura:.2f} metros")
print(f"A menor altura do grupo é: {menor_altura:.2f} metros")
print(f"A média de altura das pessoas do gênero Masculino é: {media_masculino:.2f} metros")
print(f"O número de pessoas do gênero Feminino é: {num_feminino}")

