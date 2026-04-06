# 💰 Calculadora de Gastos Personales

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Status](https://img.shields.io/badge/Estado-En%20desarrollo-yellow)
![License](https://img.shields.io/badge/Licencia-MIT-green)
![Python CI](https://github.com/JorgeLOG123/calculadora_de_gastos/actions/workflows/python-app.yml/badge.svg)  ← acá

Aplicación de consola para registrar y gestionar gastos personales en pesos argentinos con conversión automática a dólares blue en tiempo real.

> 🚧 Proyecto en desarrollo activo — crece a medida que aprendo nuevos conceptos de Python.

---

## 📋 Tabla de contenidos

- [Vista previa](#-vista-previa)
- [Funcionalidades](#-funcionalidades)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Conceptos aplicados](#-conceptos-aplicados)
- [Próximas funcionalidades](#-próximas-funcionalidades)
- [Contribuir](#-contribuir)
- [Autor](#-autor)

---

## 🖥️ Vista previa

> 📸 *(Agregá acá una captura de pantalla del programa corriendo)*

---

## ✨ Funcionalidades

- ✅ Agregar gastos con descripción, monto, categoría y fecha automática
- ✅ Listar todos los gastos registrados
- ✅ Ver el total gastado con equivalente en **dólares blue en tiempo real**
- ✅ Filtrar gastos por categoría
- ✅ Ordenar gastos de mayor a menor monto
- ✅ Persistencia de datos en JSON
- ✅ Validación de entradas con expresiones regulares

---

## ⚙️ Instalación

**Requisitos:** Python 3.12+
```bash
# 1. Clonar el repositorio
git clone https://github.com/JorgeLOG123/calculadora_de_gastos.git

# 2. Entrar a la carpeta
cd calculadora_de_gastos

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## ▶️ Uso
```bash
python main.py
```
```
===== Calculadora de Gastos =====
1) Agregar gasto
2) Lista de gastos
3) Ver total gastado
4) Filtrar por categoria
5) Ordenar gastos por monto
6) Salir
```

---

## 📁 Estructura del proyecto
```
calculadora_de_gastos/
├── main.py                   # Punto de entrada
├── models/
│   └── gasto.py              # Clase Gasto
├── services/
│   └── gastos_services.py    # Lógica de negocio
├── utils/
│   └── menu.py               # Menú de opciones
├── requirements.txt
└── .gitignore
```

---

## 🧠 Conceptos aplicados

| Concepto | Dónde se aplica |
|---|---|
| Clases y POO | `models/gasto.py` |
| `datetime` | Fecha automática al crear un gasto |
| List Comprehension | Carga de gastos desde JSON |
| Funciones Lambda | Ordenamiento y filtrado |
| `map()` `filter()` `reduce()` | Servicios de gastos |
| Manejo de ficheros JSON | Guardar y cargar gastos |
| Expresiones regulares | Validación de entradas |
| `requests` + API REST | Conversión a dólares en tiempo real |
| Git + GitHub | Control de versiones |

---

## 📌 Próximas funcionalidades

- [ ] Eliminar gastos
- [ ] Editar gastos existentes
- [ ] Filtros por fecha
- [ ] Estadísticas por categoría
- [ ] Exportar reporte a CSV

---

## 🤝 Contribuir

¡Las sugerencias son bienvenidas! Podés abrir un [issue](https://github.com/JorgeLOG123/calculadora_de_gastos/issues) o enviar un pull request.

---

## 👨‍💻 Autor

**Jorge** — [@JorgeLOG123](https://github.com/JorgeLOG123)

Basado en el curso [Hello-Python](https://github.com/mouredev/Hello-Python) de [@mouredev](https://github.com/mouredev).
