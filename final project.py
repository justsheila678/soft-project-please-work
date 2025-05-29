import flet as ft
import json
from datetime import datetime
import os

def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as f:
            return json.load(f)

def guardar_datos(data):
    with open (DATA_FILE), "w") as f:
        json.dump(data,f,indent=4)

class PresupuestoApp:
    def __init__(self, page: ft.Page):
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
        btn_nuevo = ft.ElevatedButton("Agregar Transaccion", on_click=self.nuevo_presupuesto_view)
        btn_lista = ft.ElevatedButton ("Listar Transacciones", on_click=self.listar_presupuestos_view)
        self.page.add(titulo, btn_nuevo, btn_lista)
        self.page.update()

    def nuevo_presupuesto_view(self, e):
        self.page.controls.clear()

        nombre = ft.TextField(label="Descripcion de Transaccion")
        monto = ft.TextField(label="Monto", keyboard_type=ft.KeyboardType.NUMBER)
    
        def crear_presupuesto(ev):
            
            if nombre.value and monto.value:
                self.main_view()                                                          
        
        self.page.add(
            ft.Text("Nuevo Presupuesto", size=25, weight="bold"),
            nombre,
            monto,
            ft.Row([
                ft.ElevatedButton("Crear", on_click=crear_presupuesto),
                ft.OutlinedButton("Cancelar", on_click=self.main_view)

            ])
        )
        self.page.update()
    
    def listar_presupuestos_view(self, e):
        self.page.controls.clear()
        self.page.add(ft.Text("Historial de Transacciones", size=25, weight="bold"))
 
        self.page.add(ft.OutlinedButton("Volver al Menú", on_click=self.main_view))
        self.page.update()

def main(page: ft.Page):
    PresupuestoApp(page)

ft.app(target=main)
