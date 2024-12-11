# queue_sandbox.py
from Node_sandbox import Node  # Asegúrate de que el módulo Node esté disponible
import logging

logging.basicConfig(level=logging.INFO)

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        """Agrega un valor a la cola."""
        if not self.has_space():
            logging.warning("¡Lo sentimos, no hay más espacio!") 
            return
        
        item_to_add = Node(value)
        logging.info(f"¡Agregando {item_to_add.get_value()} a la cola!")

        if self.is_empty():
            self.head = item_to_add
            self.tail = item_to_add
        else:
            self.tail.set_next_node(item_to_add)
            self.tail = item_to_add
        
        self.size += 1

    def dequeue(self):
        """Elimina y devuelve el valor en la cabeza de la cola."""
        if self.is_empty():
            logging.warning("¡Esta cola está totalmente vacía!")  
            return None
        
        item_to_remove = self.head  # Inicializa la variable con el nodo actual
        logging.info(f"¡Eliminando {item_to_remove.get_value()} de la cola!")  # Imprime el valor a eliminar
        
        if self.size == 1:  # Si solo hay un nodo
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next_node()  # Avanza la cabeza al siguiente nodo
        
        self.size -= 1  # Reduce el tamaño de la cola
        return item_to_remove.get_value()  # Devuelve el valor del nodo eliminado

    def is_empty(self):
        """Devuelve True si la cola está vacía."""
        return self.size == 0

    def get_size(self):
        """Devuelve el tamaño actual de la cola."""
        return self.size

    def has_space(self):
        """Devuelve True si hay espacio en la cola, de lo contrario False."""
        return self.max_size is None or self.max_size > self.size

    def peek(self):
        """Devuelve el valor en la cabeza de la cola sin eliminarlo."""
        if self.is_empty():
            logging.warning("¡No hay nada que ver aquí!") 
            return None
        return self.head.get_value()