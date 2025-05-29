import flet as ft

class PresupuestoApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Manejador de Presupuestos"
        self.page.window_width = 800
        self.page.window_height = 600
        self.page.horizontal_alignment = "center"
        self.page.vertical_alignment = "start"
        self.balancee = 0.0
        self.lista_de_transacciones = []
        self.main_view()
   
    def main_view(self, e=None):
        self.page.controls.clear()
        titulo = ft.Text("Menú Principal", size=30, weight="bold")
        self.total_balance_text = ft.Text(value=f"Balance Total: $ {self.balancee}", size=30, weight = "bold")
        btn_nuevo = ft.ElevatedButton("Agregar Transaccion", on_click=self.nuevo_presupuesto_view)
        btn_lista = ft.ElevatedButton ("Listar Transacciones", on_click=self.listar_presupuestos_view)
        self.page.add(titulo, self.total_balance_text, btn_nuevo, btn_lista)
        self.page.update()

    def nuevo_presupuesto_view(self, e):
        self.page.controls.clear()

        nombre = ft.TextField(label="Descripcion de Transaccion")
        monto = ft.TextField(label="Monto", keyboard_type=ft.KeyboardType.NUMBER)
        tipo_de_trans = ft.Dropdown(label="Tipo de Transacción", options=[ft.dropdown.option("Ingreso"), ft.dropdown.option("gasto")])
        
        def crear_presupuesto(ev):
            try:
                valor = float(monto.value)
                if tipo_de_trans.value == "Gasto":
                    valor= valor*-1
                elif tipo_de_trans.value == "Ingreso":
                    valor
                else:
                    self.page.bottom_sheet = ft.BottomSheet(ft.Text("Debes elegir un tipo de transaccion antes de continuar."))
                if nombre.value:
                    self.lista_de_transacciones.append((nombre.value, valor))
                    self.balance += valor
                    self.main_view()
            except ValueError:
                self.page.bottom_sheet = ft.BottomSheet(ft.Text("Introduzca un número válido."))
                self.page.bottom_sheet.open = True
                self.page.update()
                                                                    
        
        self.page.add(
            ft.Text("Nuevo Presupuesto", size=25, weight="bold"),
            nombre,
            monto,
            tipo_de_trans,
            ft.Row([
                ft.ElevatedButton("Crear", on_click=crear_presupuesto),
                ft.OutlinedButton("Cancelar", on_click=self.main_view)

            ])
        )
        self.page.update()
    
    def listar_presupuestos_view(self, e):
        self.page.controls.clear()
        self.page.add(ft.Text("Historial de Transacciones", size=25, weight="bold"))

        if not self.lista_de_transacciones:
            self.page.add(ft.Text("No hay transacciones registradas."))
        else:
            for descripcion, monto in self.lista_de_transacciones:
                self.page.add(
                ft.Text(f"{descripcion}: ${monto}")
            )
 
        self.page.add(ft.OutlinedButton("Volver al Menú", on_click=self.main_view))
        self.page.update()

def main(page: ft.Page):
    PresupuestoApp(page)

ft.app(target=main)
