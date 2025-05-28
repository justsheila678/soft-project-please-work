import flet as ft

class PresupuestoApp:
    def _init_(self, page: ft.Page):
        self.page = page
        self.page.title = "Manejador de Presupuestos"
        self.page.window_width = 800
        self.page.window_height = 600
        self.page.horizontal_alignment = "center"
        self.page.vertical_alignment = "start"
        self.main_view()
   
        def main_view(self, e=None):
            self.page.controls.clear()
            titulo = ft.Text("Menú Principal", size=30, weight="bold")
            btn_nuevo = ft.ElevatedButton(("Agregar nuevo Presupuesto"), on_click=self.nuevo_presupuesto_view)
            btn_lista = ft.ElevatedButton ("Listar Presupuestos", on_click=self.listar_presupuestos_view)
            self.page.add(titulo,btn_nuevo, btn_lista)
            self.page.update()

    def nuevo_presupuesto_view(self, e):
        self.page.controls.clear()

        nombre = ft.TextField(label="Nombre del presupuesto")
        balance = ft.TextField(label="Balance inicial", keyboard_type=ft.KeyboardType.NUMBER)
        def crear_presupuesto(ev):
            if nombre.value and balance.value:
                self.main_view(None)
        self.page.add(
            ft.Text("Nuevo Presupuesto", size=25, weight="bold"),
            nombre,
            balance,
            ft.Row([
                ft.ElevatedButton("Crear, on_click=crear_presupuesto"),
                ft.OutlinedButton("Cancelar", on_click=self.main_view)

            ])
        )
        self.page.update()

