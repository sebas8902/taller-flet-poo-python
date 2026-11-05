
import flet as ft


class ContadorApp:
    """Clase principal que encapsula la interfaz gráfica y la lógica"""

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Contador Interactivo - POO"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.valor_contador = 0
        self.crear_componentes()

    def crear_componentes(self):
        self.titulo = ft.Text(
            "Contador Interactivo",
            size=24,
            weight=ft.FontWeight.BOLD
        )

        self.texto_contador = ft.Text(
            str(self.valor_contador),
            size=60,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE
        )

        self.boton_incrementar = ft.Button(
            content="Incrementar",
            icon=ft.Icons.ADD,
            on_click=self.incrementar
        )

        self.boton_decrementar = ft.Button(
            content="Disminuir",
            icon=ft.Icons.REMOVE,
            on_click=self.decrementar
        )

        self.boton_reiniciar = ft.OutlinedButton(
            content="Reiniciar",
            icon=ft.Icons.REFRESH,
            on_click=self.reiniciar
        )

        self.page.add(
            ft.Column(
                [
                    self.titulo,
                    self.texto_contador,
                    ft.Row(
                        [
                            self.boton_decrementar,
                            self.boton_incrementar
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    self.boton_reiniciar
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25
            )
        )

    def incrementar(self, e):
        self.valor_contador += 1
        self.actualizar_contador()

    def decrementar(self, e):
        if self.valor_contador > 0:
            self.valor_contador -= 1
            self.actualizar_contador()

    def reiniciar(self, e):
        self.valor_contador = 0
        self.actualizar_contador()

    def actualizar_contador(self):
        self.texto_contador.value = str(self.valor_contador)
        self.page.update()


def main(page: ft.Page):
    app = ContadorApp(page)

if __name__ == "__main__":
    ft.run(main)
