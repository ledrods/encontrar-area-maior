comprimento_1 = int(input())
largura_1 = int(input())
comprimento_2 = int(input())
largura_2 = int(input())

area_1 = comprimento_1 * largura_1
area_2 = comprimento_2 * largura_2
maior_area = area_1
if area_2 > area_1:
  maior_area = area_2
print(maior_area)