"Archivo: stack.py"

class Stack:
    def __init__(self):
        # Usamos una lista, es este caso privada para que se pueda 
        # cumplir el encapsulamiento de la estructura.
        self.__items = []

    def push(self, item):
        """ Nos sirve para agregar un elemento  a la cima."""
        self.__items.append(item)

    def pop(self):
        """ Realiza varias tareas:
        1. Elimina y retorna el elemento en la cima.
       2. Si en un caso la pila esté vacía, retorna None.
        """
        if self.is_empty():
            return None
        return self.__items.pop()

    def peek(self):
        """Sin eliminar, puede retornar el elemento superior ."""
        if self.is_empty():
            return None
        return self.__items[-1]

    def is_empty(self):
        """Verifica si la pila no tiene elementos."""
        return len(self.__items) == 0

    def size(self):
        """Retorna la cantidad de elementos en la pila."""
        return len(self.__items)

    def clear(self):
        """Limpia todos los elementos de la pila."""
        self.__items = []

    def __str__(self):
        """Representación en texto para facilitar el debugging."""
        return f"Stack({self.__items})"



# Aquí enmpiezan las pruebas

def run_stack_tests():
    print("Iniciando pruebas unitarias de Stack...")
    
    pila = Stack()
    
    # Prueba 1: Pila vacía al inicio
    assert pila.is_empty() == True, "Error: La pila debería estar vacía"
    assert pila.size() == 0, "Error: El tamaño inicial debería ser 0"
    
    # Prueba 2: Push y Peek
    pila.push("Estado A")
    pila.push("Estado B")
    assert pila.size() == 2, "Error: El tamaño debería ser 2"
    assert pila.peek() == "Estado B", "Error: El último elemento debería ser 'Estado B'"
    
    # Prueba 3: Pop (Comportamiento LIFO)
    elemento = pila.pop()
    assert elemento == "Estado B", "Error: Pop debería devolver 'Estado B' (LIFO)"
    assert pila.size() == 1, "Error: El tamaño debería haber disminuido a 1"
    
    # Prueba 4: Manejo de casos límite (Pop en pila vacía)
    pila.pop() # Sacamos el "Estado A"
    assert pila.is_empty() == True
    resultado_nulo = pila.pop()
    assert resultado_nulo is None, "Error: Pop en pila vacía debe retornar None"
    
    # Prueba 5: Limpieza
    pila.push(100)
    pila.clear()
    assert pila.is_empty() == True, "Error: La pila debería estar limpia"

    print("¡Todas las pruebas de Stack pasaron exitosamente! ✅")

# Esto permite que el archivo se pueda importar sin que las pruebas 
# se ejecuten automáticamente a menos que corras este archivo directamente.
if __name__ == "__main__":
    run_stack_tests()