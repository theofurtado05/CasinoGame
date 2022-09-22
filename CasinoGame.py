#jogo de cassino - vermelho preto ou branco

#Funcionalidades a implementar

#Registro e Login
#Probabilidade de cada cor

#importar biblioteca
import random
import time




#variaveis
selec = 0
amount = 0 #saldo
color_list = ['preto','branco','vermelho'] #cores da roleta
verif = "s"
historico =[]
historico_apostas = [('valor da aposta','cor da aposta','resultado'),()]
#funcoes

def apresentacao():
  print("===SEJA BEM VINDO===\n")
  print("=====ao Blazheo===== \n\n")
  print("Selecione a opção que seja:\n")
  print("1- Jogar")
  print("2- Adicionar Saldo")
  print("3- Consultar saldo")
  print("4- Saque")
  print("5- Histórico de Resultados")
  print("6- Sair")
  print("7- Historico de apostas")
def options():
  print("Selecione a opção que seja:\n")
  print("1- Jogar")
  print("2- Adicionar Saldo")
  print("3- Consultar saldo")
  print("4- Saque")
  print("5- Histórico de Resultados")
  print("6- Sair")
  print("7- Historico de apostas")
  


apresentacao()
selec = int(input(""))
time.sleep(1)


#adicionar saldo
while(selec == 2): #adicionando saldo
  amount = float(input("Quanto você deseja adicionar de saldo? \n"))
  time.sleep(1)
  print("PIX GERADO - 5 min até expirar")
  time.sleep(0.3)
  print("Chave PIX - 44.495.870/0001-54")
  time.sleep(1)
  print("Processando...")
  time.sleep(1)
  print("Saldo adicionado - R$",amount)
  time.sleep(1)
  options()
  selec = int(input())

while(selec == 3):
  print("Seu saldo é de R$",amount,"\n")
  time.sleep(1)
  print("\n")
  options()
  selec = int(input(""))
  

#entrada na aposta
while (selec == 1):
  print("Entrada de aposta:")
  amount_in = float(input("Quanto você deseja apostar? ")) 


  while (amount_in > amount):
    amount_in = float(input("Digite um valor igual ou menor ao seu saldo: "))

#entrada de cor
  color_in = input("Em qual cor deseja apostar? ")
  while(color_in != color_list[0] and color_in != color_list[1] and color_in != color_list[2]):
    color_in = input("Selecione uma cor valida: ")

  print("R$",amount_in,"no", color_in)

#sortear a cor da roleta
  print("Rodando a roleta...")
  contador = 0
  while(contador != 3):
    print("...")
    contador += 1
    time.sleep(1)

  color_result = random.choice(color_list)
  

#caso de a cor escolhida, sortear novamente
  if(color_result == color_in):
    color_result = random.choice(color_list)
  elif(color_result == color_in):
      color_result = random.choice(color_list)
    
  historico.append(color_result)
  print(color_result)

#remover ou multiplicar o saldo
  if(color_in == color_list[0] and color_in == color_result):
  #preto = x2
    print("Você ganhou R$",amount_in*2,"\n")
    new_amount = (amount_in * 2) + amount
  
  elif(color_in == color_list[2] and color_in == color_result):
    #vermelho = x2
    print("Você ganhou R$",amount_in*2,"\n")
    new_amount = (amount_in * 2) + amount
  
  elif(color_in == color_list[1] and color_in == color_result):
    #branco = x14
      print("Você ganhou ",amount_in*14,"\n")
      new_amount = (amount_in*14) + amount
    
  elif(color_in != color_result):
      print("Você perdeu!\n")
      new_amount = amount - amount_in

  
  time.sleep(1)
  print("Seu novo saldo é de R$",new_amount,"\n")
  if(new_amount <= 0):
    time.sleep(1)
    print("Adicione saldo para continuar a jogar!\n")
    time.sleep(1)
    amount_in = float(input("Quanto você deseja adicionar? \n"))
    amount = amount_in
  else:
    amount = new_amount
  time.sleep(0.1)
  options()
  selec = int(input(" "))


while(selec == 4): #Saque
  print("Preencha as informações a seguir para sacar: ")
  user_name = input("Digite seu nome completo: ")
  user_cpf = input("Digite seu CPF: ")
  user_pix = input("Digite sua chave pix: ")
  user_type_pix = input("Digite o tipo de sua chave pix: ")
  contador = 0
  while(contador != 10):
    pont = "."
    print(pont)
    contador += 1
    time.sleep(0.1)
    
  user_amount_value_saque = int(input("Quanto você deseja sacar?"))
  
  contador = 0
  while(contador != 10):
    pont = "."
    print(pont*contador)
    contador += 1
    time.sleep(1)
  print("Saque efetuado! Dentro de 24hrs o valor estará em sua conta.\n\n")
  time.sleep(1)
  options()
  selec = int(input(""))


#historico
if selec == 5:
  for h in historico:
    print(h)
    time.sleep(0.5)
  print(" ")
  options()
  time.sleep(1)
  selec = int(input(" "))

if (selec == 7):
  historico_apostas.append([amount_in,color_in]) #config p/ add a aposta na lista
  for ha in historico_apostas:
    print(historico_apostas[ha])


  
if(selec == 6):
  print("Volte Sempre!")
