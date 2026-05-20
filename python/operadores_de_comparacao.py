# Operadores_de_comparacao

"""
operador  Significado          Exemplo     resultado
==        igual a              5==5        true
!=        diferente a          5!=5        false
>         mayor que            5>5         false
<         menor que            5<5         false
>=        mayor o igual que    5>=5        true
<=        menor o igual que    5<=5        true

""" 
# saldo = 200
# sague = 200

# print(saldo == sague) # esto es una función devueldendo el resultado de la comparación es verdadera
# print(saldo != sague) # esto es una función devueldendo el resultado de la comparación es falsa
# print(saldo > sague) # esto es una función devueldendo el resultado de la comparación es falsa
# print(saldo < sague) # esto es una función devueldendo el resultado de la comparación es falsa
# print(saldo >= sague) # esto es una función devueldendo el resultado de la comparación es verdadera
# print(saldo <= sague) # esto es una función devueldendo el resultado de la comparación es verdadera


"""
operador     Significado          Exemplo               resultado
and          y lógico             (2<9) and (5>3)        False
or           o lógico             (2<9) or (5>3)         True
not          no lógico            not(2<9)              False
not          no lógico            not(5>3)              False

"""

# idade = int(input("ingrese su edad: "))
# ten_carteira = input("tiene una carteira de conducir? (si/no): ")
# # para conducir se necesita tener 18 años o más y tener una carteira de conducir

# if idade >= 18 and ten_carteira == "si": 
#     print("puede conducir")
# else:
#     print("no puede conducir")




# fin_semana = bool(int(input("es fin de semana? (1 para si, 0 para no): ")))
# feriado = bool(int(input("es feriado? (1 para si, 0 para no): ")))

# # para descansar se necesita que sea fin de semana o feriado
# 0
# if feriado or fin_semana:
#     print("puede descansar")
# else:
#     print("no puede descansar")

""" 
es fin de semana? (1 para si, 0 para no): 0
es feriado? (1 para si, 0 para no): 0
no puede descansar

"""

""" Crie um programa que pergunte a nota de um aluno e imprima se ele foi aprovado ou reprovado."""

# nota = float(input("ingrese la nota del alumno: "))
# if nota >= 10:
#     print("aprobado")
# else:
#     print("reprobado")

""" 
ingrese la nota del alumno: 5
reprobado

"""

# and intervalo especifico

# x = int(input("ingresse um valor entre 1 y 10: "))
# if x >= 1 and x <= 10:
#     print("el valor esta entre 1 y 10 es: ", x)

""" 
ingresse um valor entre 1 y 10: 5
el valor esta entre 1 y 10 es: 5
"""