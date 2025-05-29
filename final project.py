import flet as ft
import json
from datetime import datetime
import os

DATA_FILE = "presupuesto.json"
def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as f:
            return json.load(f)
        return()

def guardar_datos(data):
    with open (DATA_FILE), "w" as f:
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

        nombre = ft.TextField(label="Nombre del presupuesto")
        
        def crear_presupuesto(ev):
            if nombre.value:
                nuevo_id = str(datetime.now().timestap())
                self.presupuesto[nuevo.id] = {
                    "nombre": nombre.value,
                    "gastos": [],
                    "total": 0.0
                }
                guardar_datos(self.presupuestos)
                self.main_view()
                
        self.page.add(
            ft.text("Nuevo Presupuesto", size=25, weight="bold"),
            nombre,
            ft.Row([
                ft.ElevatedButton("Crear", on_click=crear_presupuesto),
                ft.OutlinedButton("Cancelar", on_click=self.main_view)
            ])
        )
        self.page.update()

    def listar_Presupuesto(self, e):
        self.page.controls.clear()
        self.page.add(ft.Text("Presupuestos registrados", size=25, weight="bold"))

        for pid, data in self.presupuestos.items():
            fila = ft.Row([
                ft.Text(f"{data['nombre']} - total gastado: ${data['total']:.2f}"),
                ft.IconButton(icon=ft.icons.VISIBILITY, tooltip="Ver", on_click=lambda e, i=pid: self.ver_presupuesto(i)),
                ft.IconButton(icon=ft.icons.DELETE, tooltip="Eliminar", on_click=lambda e, i=pid: self.eliminar_presupuesto(i))
            ])
            self.page.add(fila)

        self.page.add(ft.OutlinedButton("Volver al menú", on_click=self.main_view))
        self.page.update()
    
    def ver_presupuesto(self, pid):
        self.page.controls.clear()
        presupuesto = self.presupuestos[pid]

        descripcion = ft.TextField(label="Descripción del gasto")
        monto = ft.Textfield(label="Monto", keyboard_type=ft.KeyboardType.NUMBER)

def agregar_gasto(e):
    if descripcion.value and monto.value:
        gasto = {
            "descripcion": descripcion.value,
            "monto": float(monto.value),
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        presupuesto["gastos"].append(gasto)
        presupuesto["total"] += gasto["monto"]
        guardar_datos(self.presupuestos)
        self.ver_presupuesto(pid)

self.page.add(
    ft.Text(f"Presupuesto: {presupuesto['nombre']}", size=25),
    ft.Text(f"Total gastado: ${presupuesto['total']:.2f}", size=1
    descripcion,
    monto,
    ft.ElevatedButton("Agregar gasto", on_click=agregar_gasto),
    ft.Divider(),
    ft.Text("Gastos:", weight="bold")
           )

def main(page: ft.Page):
    PresupuestoApp(page)
    
ft.app(target=main)
