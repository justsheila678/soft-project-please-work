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
    titulo = ft.text("Menú Principal", size=30, weight="bold"
    btn_nuevo = ft.ElevatedButton("Agregar nuevo Presupuesto"), on_click=self.nuevo_presupuesto_view)
    btn_lista = ft.ElevatedButton ("Listar Presupuestos", on_click=self.listar_presupuestos_view)
    self.page.add.(titulo,btn_nuevo, btn_lista)
    self.page.update()
