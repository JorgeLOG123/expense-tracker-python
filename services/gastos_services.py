from functools import reduce
import json
import os
from models.gasto import Gasto
import requests





def listar_gastos(gastos):
    if gastos == []:
        print("No hay nada dentro de la lista")
    else:
        for gasto in gastos:
            print(gasto)


def calcular_total(gastos):
    return reduce(lambda a, b: a + b.monto, gastos, 0)


def filtrar_por_categoria(gastos, categoria_buscada):
    resultado = list(filter(lambda g: g.categoria.lower() == categoria_buscada.lower(), gastos))
    if not resultado:
        print("No se encontraron gastos en esa categoria.")
    else:
        for gasto in resultado:
            print(gasto)


def ordenar_gastos(gastos):
    ordenados = sorted(gastos, key=lambda g: g.monto, reverse=True)
    for gasto in ordenados:
        print(gasto)


def gasto_a_diccionario(gasto):
    return {
        "id": gasto.id,
        "descripcion": gasto.descripcion,
        "monto": gasto.monto,
        "categoria": gasto.categoria,
        "fecha": gasto.fecha
    }


def guardar_gastos(gastos):
    with open("gastos.json", "w") as archivo:
        json.dump(list(map(gasto_a_diccionario, gastos)), archivo, indent=2)


def cargar_gastos():
    if os.path.exists("gastos.json"):
        with open("gastos.json", "r") as archivo:
            datos = json.load(archivo)
            return [Gasto(dato["id"], dato["descripcion"], dato["monto"], dato["categoria"]) for dato in datos]
    return []



def obtener_dolar():
    response = requests.get("https://dolarapi.com/v1/dolares")
    datos = response.json()
    blue = list(filter(lambda d: d["casa"] == "blue", datos))
    return blue[0]["venta"]  # 



def eliminar_gasto(gastos, id_eliminar):
    gasto_encontrado = list(filter(lambda g: g.id == id_eliminar, gastos))
    
    if not gasto_encontrado:
        print("No se encontro un gasto con ese ID")
    else:
       gastos.remove(gasto_encontrado[0])
       print("Gasto eliminado correctamente")