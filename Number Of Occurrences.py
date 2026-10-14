def number_of_occurrences(element, array):
    contador = 0

    for item in array:
        if item == element:
            contador += 1

    return contador