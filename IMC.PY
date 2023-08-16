altura = float(input ("digite sua altura!"))
peso = float(input("digite seu peso"))

IMC = peso/(altura*altura)

print (f"Seu IMC é {IMC:.1f}")
if IMC<=18.5:
    print("Abaixo da média")
elif IMC>=18.6 and IMC<=24.9:
    print ("Está na média")
elif IMC>=25 and IMC<=29.9:
    print ("Está com sobrepeso")
elif IMC>=30 and IMC<=34.9:
    print ("Está entrando na obesidade")
