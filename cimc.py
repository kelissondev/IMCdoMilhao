print ("Bem vindo (a) ao IMC do milhão!")

print ("Se o seu índice de massa corporal estiver entre 18.5 e 24.9, você está no caminho certo")

peso = int (input ("Digite seu peso: ") )
altura = float (input ("Digite sua altura: ") )

imc = peso / (altura * altura)

if imc < 18.5:
   print (imc)
   print ("Seu imc está abaixo de 18.5! Precisa treinar e comer muito mais")
if imc > 24.9:
    print (imc)
    print ("Seu imc está acima de 24.9! Precisa treinar e dar uma segurada na alimentação")
else:
    print (imc)
    print ("Parabéns! Você está no peso ideal")
   
print ("Obrigado por usar e cuide da saúde")

input()