def converter_unidade():
    print("Conversor de Unidades")
    print("Escolha a conversão:")
    print("1. Metros para Quilômetros")
    print("2. Quilômetros para Metros")
    print("3. Celsius para Fahrenheit")
    print("4. Fahrenheit para Celsius")
    print("5. Quilogramas para Gramas")
    print("6. Gramas para Quilogramas")
    print("7. Litros para Mililitros")
    print("8. Mililitros para Litros")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        metros = float(input("Digite o valor em metros: "))
        print(f"{metros} metros é igual a {metros / 1000} quilômetros")
    
    elif opcao == '2':
        km = float(input("Digite o valor em quilômetros: "))
        print(f"{km} quilômetros é igual a {km * 1000} metros")

    elif opcao == '3':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C é igual a {fahrenheit}°F")
    
    elif opcao == '4':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F é igual a {celsius}°C")
    
    elif opcao == '5':
        kg = float(input("Digite o valor em quilogramas: "))
        print(f"{kg} kg é igual a {kg * 1000} gramas")
    
    elif opcao == '6':
        gramas = float(input("Digite o valor em gramas: "))
        print(f"{gramas} gramas é igual a {gramas / 1000} kg")
    
    elif opcao == '7':
        litros = float(input("Digite o valor em litros: "))
        print(f"{litros} litros é igual a {litros * 1000} mililitros")
    
    elif opcao == '8':
        mililitros = float(input("Digite o valor em mililitros: "))
        print(f"{mililitros} mililitros é igual a {mililitros / 1000} litros")
    
    else:
        print("Opção inválida!")

# Função principal que permite ao usuário realizar várias conversões
def menu():
    while True:
        converter_unidade()
        continuar = input("\nDeseja realizar outra conversão? (s/n): ")
        if continuar.lower() != 's':
            print("Obrigado por usar o conversor de unidades!")
            break

if __name__ == "__main__":
    menu()
