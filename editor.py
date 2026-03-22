"Módulo: editor.py"

from stack import Stack

class TextEditor:
    def __init__(self):
        self.content = ""            # El texto actual que se ve en pantalla
        self.undo_stack = Stack()    # Pila para guarda estados anteriores
        self.redo_stack = Stack()    # Pila para guarda estados revertidos
        self.action_history = []     # Lista de strings para el registro 

    def write(self, new_text):
        """Agrega texto al contenido actual."""
        if not new_text or new_text.strip() == "":
            return False, "Error: No se puede escribir texto vacío."

        # 1. Antes de cambiar el contenido,  se guarda la info actual
        self.undo_stack.push(self.content)
        
        # 2. Al escribir algo nuevo, la pila de Redo debe limpiarse 
        if not self.redo_stack.is_empty():
            self.redo_stack.clear()

        # 3. Actualizamos el contenido y el historial
        self.content += new_text
        self.action_history.append(f"Escritura: +'{new_text}'")
        
        return True, "Texto agregado correctamente."

    def delete(self, n):
        """Elimina los últimos 'n' caracteres del contenido."""
        if n <= 0:
            return False, "Error: La cantidad de caracteres a borrar debe ser mayor a 0."

        if len(self.content) == 0:
            return False, "Error: No hay texto para borrar."

        # Guardamos  antes del borrado (SIEMPRE
        self.undo_stack.push(self.content)
        self.redo_stack.clear()

        #  Si piden borrar más de lo que hay, borramos todo
        actual_length = len(self.content)
        chars_to_remove = min(n, actual_length)
        
        deleted_text = self.content[-chars_to_remove:]
        self.content = self.content[:-chars_to_remove]
        
        self.action_history.append(f"Borrado: -'{deleted_text}' ({chars_to_remove} carac.)")
        
        if n > actual_length:
            return True, f"Aviso: Solo se borraron {actual_length} caracteres (el máximo disponible)."
        return True, f"Se borraron {chars_to_remove} caracteres."

    def undo(self):
        """Revierte a la última versión del texto guardada en la pila."""
        if self.undo_stack.is_empty():
            return False, "No hay acciones para deshacer."

        
        self.redo_stack.push(self.content) #ideal practicar mas esta funcion 
        #(es interesante)


        # Recuperamos el tope de la pila Undo
        self.content = self.undo_stack.pop()
        
        self.action_history.append("Acción: Deshacer (Undo)")
        return True, "Acción deshecha."

    def redo(self):
        """Vuelve a aplicar una acción que fue deshecha."""
        if self.redo_stack.is_empty():
            return False, "No hay acciones para rehacer."

        # El estado actual vuelve a Undo
        self.undo_stack.push(self.content)
        
        # Recuperamos el tope de la pila Redo
        self.content = self.redo_stack.pop()
        
        self.action_history.append("Acción: Rehacer (Redo)")
        return True, "Acción rehecha."

    def show(self):
        """Retorna el contenido actual del editor."""
        return self.content

    def get_history(self):
        """Retorna la lista de acciones realizadas."""
        return self.action_history




#Seccion para realizar las pruebas solicitadas y demostrar funcionabilidad
def run_editor_tests():
    print("Iniciando pruebas unitarias de TextEditor...")
    
    editor = TextEditor()

    # Prueba 1: Consta de la Escritura y validación de retorno
    exito, msg = editor.write("Hola")
    assert exito == True
    assert editor.show() == "Hola"
    
    # Prueba 2: Valida cuando el usuario ingrese una Escritura vacía
    exito, msg = editor.write("")
    assert exito == False
    assert "vacío" in msg

    # Prueba 3: Probamos la funcion Undo de manera funcional
    editor.write(" Mundo")
    editor.undo()
    assert editor.show() == "Hola", "Error en Undo: El texto debería ser 'Hola'"

    # Prueba 4: Se verifica que tambien el Redo funcione con normalidad
    editor.redo()
    assert editor.show() == "Hola Mundo", "Error en Redo: Debería ser 'Hola Mundo'"

    # Prueba 5: se hace la funcion borra pero se delimita los caracteres
    # Cuando intan borrar más de los que existen, por ejemplo 50 pero solo habían 10
    exito, msg = editor.delete(50)
    assert editor.show() == ""
    assert "Aviso" in msg
    
    # Prueba 6: Undo después de borrado total
    editor.undo()
    assert editor.show() == "Hola Mundo"

    print("¡Todas las pruebas de Lógica del Editor pasaron! ✅")

if __name__ == "__main__":
    run_editor_tests()
