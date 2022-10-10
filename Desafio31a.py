# Calcula o valor da passagem com base na distância.
d = float(input('Digite a distãncia da viagem em Km: '))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('O valor da sua passagem será de R$ {:.2f}'.format(preço))
