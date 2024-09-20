import math

# #### Números de Ponto Flutuante (`float`)


# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
valor_1 = float(input("Coloquei o primeiro valor: "))
valor_2 = float(input("Coloquei o segundo valor: "))
resultado_soma = valor_1 + valor_2
print(f'O resultado da soma dos dois números é {resultado_soma}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

valor_1 = float(input("Coloquei o primeiro valor: "))
valor_2 = float(input("Coloquei o segundo valor: "))
resultado_media = (valor_1 + valor_2)/2
print(f'A média entre os números é {resultado_media}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

valor_1 = float(input("Coloquei o valor da base: "))
valor_2 = int(input("Coloquei o valor da potência: "))
potencia = valor_1**valor_2
print(f"O valor de {valor_1} elevado a {valor_2} é {potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

valor_celsius = float(input("Coloquei o valor em Celsius: "))
conversao_em_farehain = ((9*(valor_celsius))/5)+32
print(f"O valor em farehain é {conversao_em_farehain}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# area = pi*r²

valor_raio = float(input("Coloque o valor do raio: "))
area_calculo = (math.pi*(valor_raio**2))
print(f"O valor da área com base no raio é {area_calculo:.2f} m²")