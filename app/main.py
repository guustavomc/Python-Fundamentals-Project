import json
import csv
import os

from models.book import Book
from models.customer import Customer

   
def menu_clientes():
    customers = load_customers()
    while True:
        print("\n" + "=" * 40)
        print("        GERENCIAR CLIENTES")
        print("=" * 40)
        print("1. Cadastrar cliente")
        print("2. Consultar clientes")
        print("3. Alterar cliente")
        print("4. Excluir cliente")
        print("5. Exportar para CSV")
        print("0. Voltar")
        print("-" * 40)
        opcao = input("Escolha: ").strip()

        customers = load_customers()

        if opcao == "1":
            cadastrar_cliente(customers)
        elif opcao == "2":
            consultar_clientes(customers)
        elif opcao == "3":
            alterar_cliente(customers)
        elif opcao == "4":
            excluir_cliente(customers)
        elif opcao == "5":
            exportar_clientes_csv(customers)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_principal():
    while True:
        print("\n" + "=" * 40)
        print("       SISTEMA DE LIVRARIA")
        print("=" * 40)
        print("1. Gerenciar Livros")
        print("2. Gerenciar Clientes")
        print("0. Sair")
        print("-" * 40)
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            menu_livros()
        elif opcao == "2":
            menu_clientes()
        elif opcao == "0":
            print("\nSistema encerrado. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    if login():
        menu_principal()