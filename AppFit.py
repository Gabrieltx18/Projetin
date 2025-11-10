#App: Sistema de Gerenciamento de Exercícios Físicos e Saúde
#Conectar ao MySQL

import mysql.connector

cnn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="AppFit"
)

usuario=str(input('Digite seu Nome:'))
senha=str(input('Digite sua Senha:'))

query = "Select * from user where nome = %s and senha = %s"
cursor = cnn.cursor()
cursor.execute(query, (usuario,senha))
    
usuario_encontrado = cursor.fetchone()
    
if usuario_encontrado:
    
    print("Seja bem vindo",usuario)
      
else:

    print("Usuario ou senha incorretos")
    login = input("Deseja criar uma nova conta ? (Sim / Nao) ").strip().lower()
    
    try:
        login == "Sim"

        altura= float(input('Digite sua altura em Centímetros:'))
        peso = float(input('Digite seu peso em Kg:'))
        idade = int(input('Digite sua idade:'))
        sexo = str(input('Digite seu sexo (M - Masculino | F - Feminino): ')).strip().upper()

        cmd = "INSERT INTO user (nome, senha, altura, peso, idade, sexo) VALUES (%s, %s, %s,%s, %s, %s)"
        cursor.execute(cmd, (usuario,senha,altura,peso,idade,sexo))
        
        print("Conta criada com sucesso!")
        cnn.commit()

    except Exception as  e:
        print(e)
        exit()
while True:

    print("\n=== MENU PRINCIPAL ===")
    print("1 - Registrar Exercício")
    print("2 - Calcular IMC/TMB/Gasto calórico diário")
    print("3 - Meus últimos exercícios")
    print("4 - Alterar perfil")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print('1 - Corrida (5:35 min/km)')
        print('2 - Caminhada')
        print('3 - Natação')
        print('4 - Ciclismo')
        print('5 - Musculação')

        exerc = input('Digite o número do exercício: ')

        if exerc == '0':
            print('Nenhum exercício selecionado.')

    elif opcao == "2":

        menu = input("Selecione uma das opções (IMC ou TMB): ")

        if menu.upper() == "IMC":
            imc = peso / ((altura / 100) ** 2)
            print("Seu IMC é de:",round(imc, 2))

            if imc < 18.5:
                print('Você está abaixo do peso ideal.')
            elif imc < 24.9:
                print('Você está com o peso ideal.')
            elif imc < 29.9:
                print('Você está com sobrepeso.')
            elif imc < 34.9:
                print('Você está com Obesidade Grau I.')
            elif imc < 39.9:
                print('Você está com Obesidade Grau II.')
            else:
                print('Você está com Obesidade Grau III.')

        elif menu.upper =="TMB":

            exerc_p_semana = int(input('Quantas vezes por semana você pratica exercícios físicos? '))

        if sexo == 'M':
            tmb = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
        elif sexo == 'F':
            tmb = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
        print(f'Sua taxa metabólica basal é de: {round(tmb)} kcal')

        if exerc_p_semana <= 2:
            f_ativ = 1.2
        elif exerc_p_semana <= 4:
            f_ativ = 1.35
        elif exerc_p_semana <= 6:
            f_ativ = 1.55
        else:
            f_ativ = 1.7

        media_diaria = tmb * f_ativ
        print(f'Seu gasto calórico diário estimado é de: {round(media_diaria)} kcal')



    # OPÇÃO 5 - SAIR
    elif opcao == "5":
        print("Finalizando Programa... 👋")
        break

    # OUTRAS OPÇÕES
    else:
        print("Opção inválida! Tente novamente.")
