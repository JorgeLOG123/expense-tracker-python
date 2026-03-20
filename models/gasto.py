from datetime import datetime

class Gasto:
    def __init__(self,id,descripcion,monto,categoria):
        self.descripcion = descripcion
        self.monto = monto
        self.categoria = categoria
        self.id = id
        self.fecha = datetime.now().strftime("%d/%m/%Y")
    def __str__(self):
         return f"Descripcion: {self.descripcion} | Monto: {self.monto} | Categoria: {self.categoria} | Id: {self.id} | Fecha: {self.fecha}"
       