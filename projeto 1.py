idade = int(input("qual sua idade? "))
peso = float(input("quanto você pesa em kg? "))
altura = int(input("qual a sual altura em cm? "))
genero = str(input("qual o seu genero? "))
if genero == 'masculino':
    tmb = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
else:
    tmb = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
print("sua taxa metabolca basal é de " + str(round(tmb, 2)))
altura = altura / 100
imc = peso / (altura * altura)
print("seu imc é de " + str(round(imc, 2)))
if imc <= 18.5:
    print("você está abaixo do peso ideal")
elif imc > 18.5 and imc <= 24.9:
    print("voce está no peso ideal")
elif imc > 24.9 and imc <= 30:
    print("voce está levemente acima do peso ideal")
else:
    print("você esta em estado de obesidade")
print("esses dados são uma apenas uma estimitava que não leva em consideração porcentagem de gordura, ou quantidade em kg de muscolo, etc. Para uma avaliação melhor busque um medico.")
#66 + (13,8 x peso em kg) + (5 x altura em cm) – (6,8 x idade em anos) Para as mulheres = 655 + (9,6 x peso em kg) + (1,8 x altura em cm) – (4,7 x idade em anos)