# num1 = int(input("What is your first number? "))
# num2 = int(input("What is your second number? "))
# num3 = int(input("What is your third number? "))
# numlist = [num1, num2, num3]
# print(numlist)
# print("Now I will remove the 3rd number")
# print(str(numlist.pop(2)) + " has been removed")
# print("The list now looks like " + str(numlist))

a = int(input('Insira seu saldo bancário '))
b = int(input('Insira o fator quantitativo '))
print(type(a))
soma = a + b
multiplicacao = a * b
divisao = b / a

print('Soma: {}. \nMultiplicação: {}. \nDivisão: {}'.format(soma,multiplicacao,divisao))