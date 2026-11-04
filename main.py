import flet as ft

class ContadorApp:
    """Clase principal que encapsula la interfaz gráfica y la lógica"""
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Contador Interactivo - POO"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window_width = 400
        self.page.window_height = 350
        
        self.valor_contador = 0
        self.crear_componentes()

    def crear_componentes(self):
        self.titulo = ft.Text("Contador Interactivo", size=24, weight=ft.FontWeight.BOLD)
        self.texto_contador = ft.Text(str(self.valor_contador), size=50, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE)
        
        self.boton_incrementar = ft.ElevatedButton(
            text="¡Incrementar!", 
            icon=ft.icons.ADD,
            on_click=self.manejar_clic_boton
        )
        
        self.page.add(
            ft.Column(
                [
                    self.titulo,
                    self.texto_contador,
                    self.boton_incrementar
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

    def manejar_clic_boton(self, e):
        self.valor_contador += 1
        self.texto_contador.value = str(self.valor_contador)
        self.texto_contador.update()

def main(page: ft.Page):
    app = ContadorApp(page)

if __name__ == "__main__":
    ft.app(target=main)
    