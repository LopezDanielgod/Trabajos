# Se importa la clase Node 
from Node_sandbox import Node

# Escribe debajo el codigo de la clase LinkedList y sus respectivos metodos     
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)  # Inicializa el nodo cabeza

    def get_head_node(self):
        return self.head_node  # Retorna el nodo cabeza