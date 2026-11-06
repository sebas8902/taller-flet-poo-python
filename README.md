# Taller de Investigación: Explorando Flet para Interfaces Gráficas con POO en Python

**Asignatura:** Programación Orientada a Objetos

**Tema:** Interfaces Gráficas de Usuario (GUI) y Programación Orientada a Eventos  

**Docente:** Eduardo Pimienta Leon

**Estudiante:** Sebastian De Luque Garcia 



## 1. Selección de la Biblioteca

* **Biblioteca:** [Flet](https://flet.dev/)
* **Propósito Principal:** Permitir a los desarrolladores de Python construir aplicaciones de interfaz gráfica (GUI) interactivas, modernas y multiplataforma de forma sencilla, sin necesidad de dominar tecnologías complejas de frontend como JavaScript, HTML o CSS. Flet utiliza el motor de **Flutter** por debajo para renderizar los componentes visuales de manera nativa y fluida.



## 2. Investigación

### ¿Qué tipo de aplicaciones permite desarrollar?
Flet permite crear aplicaciones de escritorio (Windows, macOS, Linux), aplicaciones web (convertibles en PWA) y aplicaciones móviles (Android e iOS) utilizando exactamente la misma base de código escrita en Python.

### ¿Cómo se instala y qué requisitos necesita?

* **Requisitos:** Tener Python instalado y el gestor de paquetes `pip`.
* **Biblioteca utilizada:** Flet 1.1.0.
* **Instalación:** Se instala desde la terminal ejecutando:

  ```bash
  pip install flet==1.1.0
  ```

### ¿Cómo maneja los eventos del usuario?

Flet utiliza un sistema de eventos que permite ejecutar funciones o métodos cuando el usuario interactúa con los componentes de la interfaz. Por ejemplo, la propiedad `on_click` permite detectar cuando se presiona un botón y ejecutar una función asociada.

En este proyecto, cada botón tiene un evento `on_click` vinculado a un método de la clase `ContadorApp`, permitiendo incrementar, disminuir (hasta el 0) o reiniciar el contador según la acción realizada por el usuario.
  
### ¿Cuáles son sus principales componentes o elementos gráficos?

Flet organiza la interfaz mediante controles visuales que permiten construir aplicaciones interactivas:

* `ft.Page`: Representa la página principal de la aplicación.
* `ft.Text`: Permite mostrar textos estáticos o dinámicos.
* `ft.Button`: Crea botones interactivos.
* `ft.OutlinedButton`: Crea botones con estilo de contorno.
* `ft.Row`: Organiza los elementos horizontalmente.
* `ft.Column`: Organiza los elementos verticalmente.

En este proyecto se utilizan estos componentes para mostrar el contador y permitir que el usuario interactúe con sus funcionalidades. 

### ¿Qué ventajas y limitaciones presenta frente a Tkinter y Pygame?

| Criterio | Flet | Tkinter | Pygame |
| :--- | :--- | :--- | :--- |
| **Diseño** | Moderno, basado en Flutter y Material Design. | Clásico y sencillo. | Orientado a gráficos, animaciones y videojuegos. |
| **Multiplataforma** | Escritorio, web y móvil. | Principalmente escritorio. | Principalmente escritorio. |
| **Facilidad de uso** | Permite crear interfaces sin conocimientos avanzados de frontend. | Sencillo para proyectos básicos. | Requiere comprender el manejo de gráficos y eventos. |
| **Eventos** | Utiliza propiedades como `on_click` para responder a interacciones. | Utiliza mecanismos como `command` y `bind`. | Utiliza un sistema de eventos para detectar clics y pulsaciones del teclado. |
| **Elementos gráficos** | Botones, textos, campos y otros controles visuales. | Botones, etiquetas, cuadros de texto y otros controles. | Imágenes, figuras, sprites y elementos gráficos. |
| **Consumo de recursos** | Puede requerir más recursos por su arquitectura. | Generalmente ligero. | Depende de la complejidad de los gráficos y del juego. |



## 3. Explicación del Ejemplo y Orientación a Objetos

### Explicación del Funcionamiento

La aplicación consiste en un contador interactivo que permite aumentar, disminuir y reiniciar un valor numérico mediante una interfaz gráfica.

1. **Creación de la Ventana Principal:** Se obtiene una instancia de `ft.Page` mediante la función `main(page)`, donde se crea un objeto de la clase `ContadorApp`.

2. **Inicialización del Contador:** El atributo `self.valor_contador` comienza con el valor cero y almacena el estado actual del contador.

3. **Creación de Componentes Gráficos:** Se utilizan controles como `ft.Text`, `ft.Button` y `ft.OutlinedButton` para mostrar el título, el valor del contador y los botones de interacción.

4. **Organización de la Interfaz:** Los componentes se organizan mediante `ft.Column` y `ft.Row`, permitiendo distribuir los elementos vertical y horizontalmente.

5. **Detección de Eventos:** Cada botón utiliza la propiedad `on_click` para vincular la interacción del usuario con un método de la clase.

6. **Respuesta al Evento:** Los métodos `incrementar()`, `decrementar()` y `reiniciar()` modifican el valor del contador y llaman a `actualizar_contador()` para reflejar los cambios en pantalla.

### Reto Adicional: Estructura Orientada a Objetos (POO)

La aplicación fue desarrollada encapsulando la lógica y los componentes gráficos dentro de la clase `ContadorApp`:

- **Atributos de Estado:** `self.valor_contador` almacena el valor numérico actual del contador.

- **Atributos Visuales:** `self.titulo`, `self.texto_contador`, `self.boton_incrementar`, `self.boton_decrementar` y `self.boton_reiniciar` mantienen las referencias a los componentes gráficos.

- **Métodos:** `crear_componentes()` construye la interfaz; `incrementar()`, `decrementar()` y `reiniciar()` controlan las operaciones del contador; `actualizar_contador()` actualiza el valor mostrado en pantalla.

- **Encapsulamiento:** La clase `ContadorApp` agrupa los atributos y métodos necesarios para el funcionamiento del contador, permitiendo que la lógica y la interfaz estén organizados dentro de una misma estructura.

- **Validación:** El método `decrementar()` contiene una condición que impide que el contador tome valores negativos.



## 4. Instrucciones de Instalación y Ejecución

1. **Clonar el repositorio:** 
   ```bash
   git clone https://github.com/sebas8902/taller-flet-poo-python.git

   cd taller-flet-poo-python
   ```

2. **Instalar dependencias:**
   ```bash
   pip install flet==1.1.0
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```



## 5. Evidencia de Funcionamiento

![Captura de pantalla de la app](evidencia.png)

### Funcionalidades implementadas

* **Incrementar:** Aumenta el valor del contador en una unidad.
* **Disminuir:** Reduce el valor del contador en una unidad, sin permitir valores negativos.
* **Reiniciar:** Restablece el contador a cero.

### Fuentes Consultadas
1. Flet Developer Documentation: [https://flet.dev/docs/](https://flet.dev/docs/)
2. Flet GitHub Repository: [https://github.com/flet-dev/flet](https://github.com/flet-dev/flet)
3. Python Package Index (PyPI) - Flet: [https://pypi.org/project/flet/](https://pypi.org/project/flet/)
4. Pygame Official Documentation: [https://www.pygame.org/docs/](https://www.pygame.org/docs/)
