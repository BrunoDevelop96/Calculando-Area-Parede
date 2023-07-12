#-----------------------------Exercicio----------------------------------------------------

#Programa para calcular a largura e altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la ,
#sabendo que a cada litro de tinta, pinta uma área de 2m²

#-------------------------------------------------------------------------------------------

print("")
altura = float(input("Qual a altura da parede? "))
print("")
largura = float(input("Qual a largura da parede? "))
areaTotal = altura * largura
pintar = areaTotal / 2
print("")
print("A dimensão da sua parede é : {} x {} e uma área total de : {}m² ".format(altura, largura, areaTotal))

print("Para pintar essa parede você precisara de {} litros".format(pintar))