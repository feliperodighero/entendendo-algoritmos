def buscar_menor(array):
    menor = array[0]
    menor_indice = 0
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
    return menor_indice

def ordenar_por_selecao(array):
    novo_array = []
    for i in range(len(array)):
        menor = buscar_menor(array)
        print(f"Menor elemento encontrado: {array[menor]} na posição {menor}")
        novo_array.append(array.pop(menor))
        print(f"Array atualizado: {array}")
    return novo_array

print(ordenar_por_selecao([5, 3, 6, 2, 10]))
