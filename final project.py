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