#tamanho em m² da área a ser pintada
area = float(input('Digite o tamanho da área a ser pintada (em m²): '))
print(f'Área a ser pintada: {(area):.0f}m²')
#cobertura de tinta:
    #1 litro para 3 m²
litro = area / 3
lata_maior = area / 18
    #1 lata de tinta = 18 litros = R$ 80.00
valor_lata = 80
valor_lata = float(valor_lata)

#quantas latas precisam ser compradas
#qual o preço total a se pagar
if litro < 18:
    print(f'Comprar somente 1 lata de 18 litros.')
    print(f'Serão necessários somente {(litro):.0f} litros para pintar {(area):.0f}m²')
    print(f'Total a pagar: 1 lata de 18 litros = R$ {(valor_lata):.2f}')
elif litro >= 18:
    print(f'Precisam ser compradas {(lata_maior):.0f} latas.')
    print(f'Serão {(litro):.0f} litros para {(area):.0f}m²')
    print(f'Total a pagar: R$ {(lata_maior * valor_lata):.2f}')
else:
    print('Valor Inválido')
