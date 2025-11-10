import mysql.connector

cnn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="AppFit"
)

usuario = str(input('Digite seu Nome: '))
senha = str(input('Digite sua Senha: '))

query = "SELECT id, nome, altura, peso, idade, sexo FROM user WHERE nome = %s AND senha = %s"
cursor = cnn.cursor()
cursor.execute(query, (usuario, senha))

usuario_encontrado = cursor.fetchone()

if usuario_encontrado:
    print("Seja bem-vindo", usuario)
    id_usuario, nome, altura, peso, idade, sexo = usuario_encontrado

else:
    print("Usuário ou senha incorretos")
    login = input("Deseja criar uma nova conta ? (Sim / Nao) ").strip().lower()

    try:
        login == "Sim"

        altura = float(input('Digite sua altura em Centímetros: '))
        peso = float(input('Digite seu peso em Kg: '))
        idade = int(input('Digite sua idade: '))
        sexo = str(input('Digite seu sexo (M - Masculino | F - Feminino): ')).strip().upper()

        cmd = "INSERT INTO user (nome, senha, altura, peso, idade, sexo) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(cmd, (usuario, senha, altura, peso, idade, sexo))

        print("Conta criada com sucesso!")
        id_usuario = cursor.lastrowid
        cnn.commit()

    except Exception as e:
        print(e)
        exit()

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Registrar Exercício")
    print("2 - Calcular IMC/TMB/Gasto calórico diário")
    print("3 - Meus últimos exercícios")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exercicios = {
            "1": "Corrida (5:35 min/km)",
            "2": "Caminhada",
            "3": "Natação",
            "4": "Ciclismo"
        }

        exerc = input('Digite o número do exercício: ')

        if exerc in exercicios:
            nome_exercicio = exercicios[exerc]

        duracao = float(input('Digite a duração do exercício em minutos: '))
        ritimo = float(input('Digite o ritmo médio (min/km): '))
        intensidade = input('Digite a intensidade (leve, moderada, intensa): ').strip().lower()

        cmd = "INSERT INTO atv_cardio (nome_atv, tempo_atv, ritimo_medio, id_usuario) VALUES (%s, %s, %s, %s)"
        cursor.execute(cmd, (nome_exercicio, duracao, ritimo, id_usuario))
        cnn.commit()

        if exerc == '5':
            exercicio_nome = str(input('Digite o nome do exercício de : '))
            peso_exerc = float(input('Digite o peso levantado em Kg: '))
            repeticoes = int(input('Digite o número de repetições: '))
            series = int(input('Digite o número de séries: '))
            tempo_treino = float(input('Digite o tempo total de treino em minutos: '))

            resultado = cursor.fetchone()

            met = 6.0
            gasto_calorico = (met * peso * tempo_treino)

            cmd = "INSERT INTO ficha (nm_exercicio, peso, repeticoes, series, gasto_calorico, id_usuario) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(cmd, (exercicio_nome, peso_exerc, repeticoes, series, gasto_calorico, id_usuario))
            cnn.commit()

    elif opcao == "2":
        menu = input("Selecione uma das opções (IMC ou TMB): ")

        if menu.upper() == "IMC":
            imc = peso / ((altura / 100) ** 2)
            print("Seu IMC é de:", round(imc, 2))

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

        elif menu.upper() == "TMB":
            exerc_p_semana = int(input('Quantas vezes por semana você pratica exercícios físicos? '))

            if sexo == 'Masculino':
                tmb = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
            elif sexo == 'Feminino':
                tmb = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

            print("Sua taxa metabólica basal é de:", round(tmb), "kcal")

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

    elif opcao == "4":
        print("Finalizando Programa... 👋")
        break

    else:
        print("Opção inválida! Tente novamente.")
