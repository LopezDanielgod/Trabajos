from Node import Node  

import logging

# Configuración del registro para manejar mensajes de advertencia e información
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None  # Nodo superior de la pila
        self.size = 0         # Número actual de elementos en la pila
        self.limit = limit    # Capacidad máxima de la pila

    # Verifica si la pila tiene espacio disponible
    def has_space(self):
        return self.size < self.limit

    # Verifica si la pila está vacía
    def is_empty(self):
        return self.size == 0

    # Devuelve el elemento superior sin eliminarlo
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()  # Valor del nodo superior
        else:
            logging.warning("La pila está vacía.")  
            return None

    # Agrega un elemento en la parte superior de la pila
    def push(self, value):
        if self.has_space():
            item = Node(value)  # Crea un nuevo nodo
            item.set_next_node(self.top_item)  # Apunta al nodo actual superior
            self.top_item = item  # Actualiza el nodo superior
            self.size += 1        # Incrementa el tamaño de la pila
        else:
            logging.warning("La pila está llena. No se puede agregar más elementos.")

    # Elimina y devuelve el elemento superior de la pila
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item  # Nodo que se eliminará
            self.top_item = item_to_remove.get_next_node()  # Actualiza el nodo superior
            self.size -= 1  # Decrementa el tamaño de la pila
            return item_to_remove.get_value()  # Devuelve el valor eliminado
        else:
            logging.warning("La pila está vacía. No se puede eliminar ningún elemento.")
            return None




















if __name__ == "__main__":
    # Crear una pila con un límite de 5 elementos
    stack = Stack(limit=5)

    # Agregar elementos a la pila
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Mostrar el elemento superior sin eliminarlo
    print("Elemento superior:", stack.peek())  # Salida: 30

    # Eliminar elementos de la pila
    print("Elemento eliminado:", stack.pop())  # Salida: 30
    print("Elemento eliminado:", stack.pop())  # Salida: 20

    # Mostrar el estado actual de la pila
    print("Elemento superior después de eliminaciones:", stack.peek())  # Salida: 10

    # Agregar más elementos hasta llenar la pila
    stack.push(40)
    stack.push(50)
    stack.push(60)  # Este se agrega correctamente
    stack.push(70)  # Este no se agrega (límite alcanzado)

    # Vaciar completamente la pila
    while not stack.is_empty():
        print("Elemento eliminado:", stack.pop())

    # Intentar eliminar de una pila vacía
    print("Intentar eliminar de una pila vacía:", stack.pop())