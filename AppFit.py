#App: Sistema de Gerenciamento de Exercícios Físicos e Saúde
#Conectar ao MySQL

#import mysql.connector
#conn = mysql.connector.connect(
#    host="localhost",
#    user="seu_usuario",
#    password="sua_senha",
#    database="seu_banco_de_dados")

#Definir usuario e senha
usuario=str(input('Digite seu Nome:'))
senha=str(input('Digite sua Senha:'))
print(f'Bem vindo {usuario}, vou precisar de algumas informações\n para calcular sua taxa metabolica basal.')
#Dados do usuario
altura=int(input('Digite sua altura em Centímetros:'))
peso=float(input('Digite seu peso em Kg:'))
idade=float(input('Digite sua idade:'))
sexo = None
while True:
    sexo = input('Digite seu sexo (M - Masculino | F - Feminino): ').strip().upper()
    if sexo in ['M', 'MASCULINO']:
        sexo = 'M'
        break
    elif sexo in ['F', 'FEMININO']:
        sexo = 'F'
        break
    else:
        print('Opção inválida! Digite M, Masculino, F ou Feminino.')
# Definir fator de atividade física conforme quantidade de práticas
exerc_p_semana = int(input('Quantas vezes por semana você pratica exercícios físicos? '))
# Calcular taxa metabolica basal
if sexo=='M':
    tmb=66+(13.7*peso)+(5*altura)-(6.8*idade)
    print(f'Sua taxa metabolica basal é de: {round(tmb)}')
elif sexo=='F':
    tmb=655+(9.6*peso)+(1.8*altura)-(4.7*idade)
    print(f'Sua taxa metabolica basal é de: {round(tmb)}')
#Media calculada de calorias gastas em um dia todo
if exerc_p_semana <= 2:
    f_ativ = 1.2
elif exerc_p_semana <= 4:
    f_ativ = 1.35
elif exerc_p_semana <= 6:
    f_ativ = 1.55
elif exerc_p_semana >= 7:
    f_ativ = 1.7
media_diaria = tmb * f_ativ
print(f'Seu gasto estimado calórica diária é de: {round(media_diaria)}kcal.')
#calcular o imc da pessoa 
imc = peso / ((altura / 100) ** 2)
print(f'Seu IMC é de: {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= imc < 24.9:
    print('Você está com o peso ideal.')
elif 25 <= imc < 29.9:
    print('Você está com sobrepeso.')
elif 30 <= imc < 34.9:
    print('Você está com Obesidade Grau I.')
elif 35 <= imc < 39.9:
    print('Você está com Obesidade Grau II.')
elif imc >= 40:
    print('Você está com Obesidade Grau III.')
# Definir 5 exercicios diferentes
print('Agora vamos calcular o gasto calórico do seu exercício físico.')
print('Qual o exercício que você praticou?')
print('0 - Nenhum')
print('1 - Corrida (5:35 min/km)')
print('2 - Caminhada')
print('3 - Natação')
print('4 - Ciclismo')
print('5 - Musculação')
exerc = input('Digite o número do exercício: ')
if exerc == '0':
    print('Nenhum exercício selecionado.')
    input("Pressione Enter para sair...")
    exit()
tempo = float(input('Digite o tempo de exercício em minutos: '))
# METs para os 5 exercícios principais
met_dict = {
    '1': 10.5, # Corrida (5:35 min/km)
    '2': 4.0,  # Caminhada
    '3': 8.0,  # Natação
    '4': 7.0,  # Ciclismo
    '5': 6.0   # Musculação
}
if exerc in met_dict:
    met = met_dict[exerc]
    gasto = met * peso * (tempo / 60)
    print(f'O gasto calórico do seu exercício é de: {round(gasto)} kcal.')
else:
    print('Opção inválida. Encerrando o programa.')
    exit()
input("Pressione Enter para sair...")

#Adiciona mais exercicios
#Cria uma forma mais facil de transforma em .exe do programa
   #python -m PyInstaller --onefile Projetin.py