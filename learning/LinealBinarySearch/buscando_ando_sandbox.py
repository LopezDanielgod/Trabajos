def sparse_search(data, search_val):
    print("Datos: " + str(data))
    print("Valor de búsqueda: " + str(search_val))

    first = 0
    last = len(data) - 1

    while first <= last:
        mid = (first + last) // 2

        # Comprobar si el medio está vacío
        if data[mid] == "":
            left = mid - 1
            right = mid + 1

            # Buscar valores circundantes
            while True:
                if left < first and right > last:
                    print(f"{search_val} no está en el conjunto de datos.")
                    return

                # Comprobar el valor a la derecha
                if right <= last and data[right] != "":
                    mid = right
                    break
                # Comprobar el valor a la izquierda
                elif left >= first and data[left] != "":
                    mid = left
                    break

                # Si no se encontró un valor no vacío, mover punteros
                right += 1
                left -= 1

        # Verificar si el medio es igual al valor de búsqueda
        if data[mid] == search_val:
            print(f"{search_val} encontrado en la posicion {mid}.")  # Sin tilde
            return mid

        # Ajustar los punteros según el valor de búsqueda
        elif search_val < data[mid]:
            last = mid - 1
        else:
            first = mid + 1

    print(f"{search_val} no está en el conjunto de datos.")
    return