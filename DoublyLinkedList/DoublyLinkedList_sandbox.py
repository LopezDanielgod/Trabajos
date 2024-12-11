# Escribe debajo el codigo de la clase DoublyLinkedList y sus respectivos metodos     
# Recuerda importar la clase Node en este script
from Node_sandbox import Node  

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        if self.head_node is not None:
            new_head.next_node = self.head_node
            self.head_node.prev_node = new_head
        self.head_node = new_head
        if self.tail_node is None:  
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        if self.tail_node is not None:
            new_tail.prev_node = self.tail_node
            self.tail_node.next_node = new_tail
        self.tail_node = new_tail

        if self.head_node is None:  
            self.head_node = new_tail

    def remove_head(self):
        if self.head_node is None:
            return None
        removed_node = self.head_node
        self.head_node = removed_node.next_node
        if self.head_node is not None:
            self.head_node.prev_node = None
        else:
            self.tail_node = None  
        return removed_node  # Devolver el nodo eliminado

    def remove_tail(self):
        if self.tail_node is None:
            return None
        removed_node = self.tail_node
        self.tail_node = removed_node.prev_node
        
        if self.tail_node is not None:
            self.tail_node.next_node = None
        else:
            self.head_node = None 
        return removed_node  # Devolver el nodo eliminado

    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node
        
        while current_node is not None:
            if current_node.value == value_to_remove:
                node_to_remove = current_node
                break
            current_node = current_node.next_node
        
        if node_to_remove is None:
            return None
        
        if node_to_remove == self.head_node:
            self.head_node = node_to_remove.next_node
            if self.head_node is not None:
                self.head_node.prev_node = None
            else:
                self.tail_node = None
            return node_to_remove  # Devolver el nodo eliminado
        
        if node_to_remove == self.tail_node:
            self.tail_node = node_to_remove.prev_node
            if self.tail_node is not None:
                self.tail_node.next_node = None
            else:
                self.head_node = None
            return node_to_remove  # Devolver el nodo eliminado
        
        prev_node = node_to_remove.prev_node
        next_node = node_to_remove.next_node
        prev_node.next_node = next_node
        if next_node is not None:
            next_node.prev_node = prev_node
        
        return node_to_remove  # Devolver el nodo eliminado