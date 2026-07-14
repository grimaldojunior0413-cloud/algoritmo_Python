#Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

#Entrada
#O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

#Saída
#Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

A = input("Coloque seu nome aqui: ")
B= float(input("Coloque quanto você vendeu:"))
C = 1230.30
D = 0.15
Comi = B * D
resultado = C + Comi
print(A)
print(f"salario fixo: {C:.2f}")
print(f"O total da comição: {Comi:.2f}")
print(f"TOTAL = R$ {resultado:.2f}")+