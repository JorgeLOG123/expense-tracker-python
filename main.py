from utils.menu import mostrar_menu
from models.gasto import Gasto
from services.gastos_services import listar_gastos, calcular_total, filtrar_por_categoria, ordenar_gastos, cargar_gastos, guardar_gastos, obtener_dolar, eliminar_gasto
import re
gastos = cargar_gastos()
siguiente_id =  max(gasto.id for gasto in gastos) + 1 if gastos else 1
pattern = r"[a-zA-Z]"

while True:
    mostrar_menu()
    
    opcion = input("Escoge una opcion: ")
    
    if opcion == "1":
        print("=== Añade los siguentes valores ===")
        
        descripcion = input("Ingrese la descripción: ")
        if re.search(r"[a-zA-Z]", descripcion):
            try:
                monto = int(input("Ingrese el monto: "))
            except ValueError:
                print("El monto tiene que ser un valor de tipo numero")
            else:
                categoria = input("Ingrese la categoría: ")
                nuevo_gasto = Gasto(siguiente_id, descripcion, monto, categoria)
                gastos.append(nuevo_gasto)
                siguiente_id += 1
                print("Gasto agregado")
                guardar_gastos(gastos)
        else:
            print("Error: ingrese al menos un carácter")

    elif opcion == "2":
        listar_gastos(gastos)

    elif opcion == "3":
        total = calcular_total(gastos)
        print(f"Total gastado: {total}")
        dolar = obtener_dolar()
        print(f"Total gastado: ${total} ARS")
        print(f"Equivalente:   ${total / dolar:.2f} USD (dólar blue: ${dolar})")
        
    elif opcion == "4":
        categoria_buscada = input("Ingrese la categoría a buscar: ")
        filtrar_por_categoria(gastos, categoria_buscada)
       
    elif opcion == "5":
        ordenar_gastos(gastos)
    
  
    elif opcion == "6":
        id_eliminar = int(input("Ingrese el ID del gasto a eliminar: "))
        eliminar_gasto(gastos, id_eliminar)
        guardar_gastos(gastos)
  
  
    elif opcion == "7":
        print("Saliendo del sistema, adios!:)")
        break
    else:
        print("Opcion invalida")


