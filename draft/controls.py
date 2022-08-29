from database import *

#Menu Principal
def menu():
    menu = ("[1] Nova Transação\n[2] Listar Transações\n[3] Remover Transação\n[4] Extrado\n[5] Exportar Relatório\n[0] Resetar Valores\n[9] Encerrar\n")
    print(menu)

#[1] Nova Transação
def newTransaction():
    print("-"*20)
    print("\nPreencha da seguinte forma DDMMAAAA\nExemplo: 12032022\n")
    date = int(input("Informe a data da transação:\n-->   "))

    print("-"*20)
    print("\n[1] Entrada\n[2] Saída\n")
    operation = int(input("Tipo da transação:\n-->   "))

    print("-"*20)
    print("\nDigite uma breve descrição para transação\n")
    description = str(input("Descrição:\n-->   "))

    print("-"*20)
    print("\nPreencha da seguinte forma 0.00\n")
    value = float(input("Valor da transção:\n-->   "))

    #Válida Tipo de Operação
    if operation == 1:
        operation = "entrada"
    elif operation == 2:
        operation = "saida"

    #Lista Dados da Transação
    new = Transaction(date = date, operation = operation, description = description, value = value)
    #Salva Transação no Banco
    new.save()

    print("\n\n")
    print(f"Transação Salva\n{date} - {operation} - {description} - {value}")
    print("\n\n")

#[2] Listar Transação
def showTransaction():
    query = Transaction.select().where(Transaction.operation != "none")
    print("\n\n")
    print("ID, DATA, OPERAÇÃO, DESCRIÇÃO, VALOR")
    for data in query:
        transaction = data.id, data.date, data.operation, data.description, data.value
        print(transaction)
    print("\n\n")

#[3] Remover Transação
def removeTransaction():
    query = Transaction.select().where(Transaction.operation != "none")
    print("\n\n")
    print("ID, DATA, OPERAÇÃO, DESCRIÇÃO, VALOR")
    for data in query:
        transaction = data.id, data.date, data.operation, data.description, data.value
        print(transaction)
    print("\n")
    print("-"*20)
    print("\nDigite o ID da Transação para remover\n")
    user = int(input("Tipo da transação:\n-->   "))
    remove = Transaction.get(Transaction.id == user)
    remove.delete_instance()
    print(f"\nTransação {user}, removida com sucesso!\n")

#[4] Extrado
def extract():
    #Renda
    query = Transaction.select().where(Transaction.operation == "entrada")
    incomes = 0
    for inc in query:
        incomes += inc.value
    print(f"\nRenda: {incomes}")

    #Despesa
    query = Transaction.select().where(Transaction.operation == "saida")
    expenses = 0
    for exp in query:
        expenses += exp.value
    print(f"Despesas: {expenses}")

    #Saldo Total 
    balance = incomes - expenses
    print(f"\nSaldo Total: {balance}")

    #Total de Operações
    query = Transaction.select().where(Transaction.operation != "none")
    operation = (query.count())
    print(f"Total de Operações: {operation}\n")

#[5] Exportar Relatório
def report():
    file = open("transactions.txt", "a")

    #Cabecalho
    file.write("FINANCE$.dev\nGerencie seus gastos\n" + "-"*20 + "\n")

    #Renda
    query = Transaction.select().where(Transaction.operation == "entrada")
    incomes = 0
    
    file.write("\n#RENDA\n")
    file.write("ID, DATA, OPERAÇÃO, DESCRIÇÃO, VALOR\n")
    for inc in query:
        transaction = inc.id, inc.date, inc.operation, inc.description, inc.value
        file.write(f"{transaction}\n")
    for inc in query:
        incomes += inc.value
    
    file.write("\n" + "-"*40 + "\n")

    #Despesa
    query = Transaction.select().where(Transaction.operation == "saida")
    expenses = 0
    file.write("\n#DESPESAS\n")
    file.write("ID, DATA, OPERAÇÃO, DESCRIÇÃO, VALOR\n")
    for exp in query:
        transaction = exp.id, exp.date, exp.operation, exp.description, exp.value
        file.write(f"{transaction}\n")
    for exp in query:
        expenses += exp.value

    file.write("\n" + "-"*40 + "\n")

    #Saldo Total
    balance = incomes - expenses
    file.write(f"\nSaldo Total: {balance}")

    file.write("\n" + "-"*20)

    #Total de Operações
    query = Transaction.select().where(Transaction.operation != "none")
    operation = (query.count())
    file.write(f"\nTotal de Operações: {operation}\n")

    file.close()

    print("\nRelatório concluido com sucesso!\n")

#[0] Resetar Valores
def resetTransaction():
    reset = Transaction.select().where(Transaction.id != "none")
    for data in reset:
        remove = Transaction.get(Transaction.id == data)
        remove.delete_instance()
    print("\nTransações removida com sucesso!\n")

#[9] Encerrar
def close():
    print("\nFinalizando ...")
    quit()
    