                                     **Simulador-de-editor-con-historial-de-acciones-usando-pilas**

#¿Qué hace el programa? = Este programa permite al usuario escribir y editar texto mediante una interfaz gráfica, incluyendo                                        funcionalidades de deshacer (undo) y rehacer (redo), simulando el comportamiento de un editor real.

#Objetivo: Realizar una simulación de un editor de texto funcional que utiliza la estructura de datos "Stack" (Pila) para                            gestionar operaciones de escritura, borrado, deshacer (undo) y rehacer (redo).

# Estructura del proyecto: 
 - "stack.py": En este módulo se implementó la estructura de datos Stack.
 - "editor.py": Esta parte del proyecto sirvio como el modulo Lógico del editor, donde se incluyen las funciones undo, redo, escritura y                  borrado.
  - "main.py": En esta seccion se trabajó el area visual, es decir la Interfaz gráfica, utilizando Tkinter; dando un aspecto profesional                 y limpio para el usuario.
  
---------------------------------------------------------------------------------------------------------------------------
##  Conceptos de Estructura de Datos Aplicados

# 1. Implementación de la Pila (Stack)

Se desarrolló una clase propia  llamada "Stack" en el módulo "stack.py" que encapsula una lista de Python. Esta clase sigue el principio **LIFO** (Last In, First Out), exponiendo únicamente los métodos esenciales:
- "push(item)": Agrega un estado a la cima.
- "pop()": Remueve y retorna el elemento superior.
- "peek()", "is_empty()" y "size()": Para control de flujo.

# 2. Lógica de Undo y Redo
El sistema utiliza dos pilas independientes para gestionar los estados del texto:
* "Undo Stack:" Al realizar una acción (escritura o borrado), el contenido actual se guarda en esta pila antes de ser modificado.
* "Redo Stack": Cuando el usuario presiona "Deshacer", el estado actual se mueve a esta pila. Esto permite "volver" si el                                 usuario decide reaplicar la acción.
---------------------------------------------------------------------------------------------------------------------------

# Validaciones y Manejo de Errores
El software está diseñado para ser robusto ante entradas inesperadas:
- "Borrado excedente" Si se intenta borrar más caracteres de los existentes, el sistema ajusta el valor automáticamente para borrar el                          contenido disponible sin romper el programa.
- "Entradas vacías:" Se valida que no se procesen cadenas vacías en la función de escritura.
- "Pilas Vacías:" Los métodos Undo/Redo verifican si la pila tiene elementos antes de operar, evitando errores de índice.
- "Tipos de datos:" La interfaz captura errores de tipo (ej. ingresar letras en el contador de borrado) mediante bloques "try-except".

---------------------------------------------------------------------------------------------------------------------------

# Interfaz Gráfica (GUI)
Desarrollada con "Tkinter" la interfaz separa la lógica de la presentación. 
- "Estilo: " Paleta de colores pastel (Azul, Amarillo, Verde Limón) con fuente *Century Gothic*.
- "Seguridad:" El área de texto es de solo lectura para el usuario; toda modificación debe pasar obligatoriamente por los métodos de la                  clase "TextEditor", garantizando que el historial siempre se registre.


![Interfaz gráfica del editor de texto](img/imagen_proyecto.png)

---------------------------------------------------------------------------------------------------------------------------

# Pruebas Unitarias
El proyecto incluye validaciones integradas mediante assert para garantizar la integridad de los datos:
- Pruebas de Stack:  Verificación de comportamiento LIFO y manejo de nulos.
- +Pruebas de Editor:  Validación de flujo Undo -> Redo y límites de borrado.

Para ejecutar las pruebas, corre en terminal:
"python stack.py" y "python editor.py"

---------------------------------------------------------------------------------------------------------------------------

# Cómo ejecutar
1. Asegúrate de tener Python 3.12+.
2. Descarga los archivos: "stack.py", "editor.py" y "main.py".
3. Ejecuta: "python main.py"

---------------------------------------------------------------------------------------------------------------------------
