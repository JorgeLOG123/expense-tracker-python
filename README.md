💰 Calculadora de Gastos Personales
Proyecto desarrollado en Python para registrar y gestionar gastos personales. Comenzó como un proyecto simple y fue creciendo a medida que fui aprendiendo nuevos conceptos del lenguaje.

🚀 Funcionalidades

✅ Agregar gastos con descripción, monto, categoría y fecha automática
✅ Listar todos los gastos registrados
✅ Ver el total gastado (con equivalente en dólares blue en tiempo real)
✅ Filtrar gastos por categoría
✅ Ordenar gastos de mayor a menor monto
✅ Persistencia de datos en archivo JSON
✅ Validación de entradas con expresiones regulares


🧠 Conceptos aplicados
Este proyecto fue creciendo con cada lección aprendida:
ConceptoDónde se aplicaClases y POOmodels/gasto.pydatetimeFecha automática al crear un gastoList ComprehensionCarga de gastos desde JSONFunciones LambdaOrdenamiento y filtradomap()Conversión de objetos a diccionariosfilter()Filtrado por categoríareduce()Cálculo del total gastadoManejo de ficheros JSONGuardar y cargar gastosExpresiones regularesValidación de descripción y categoríarequests + API RESTConversión a dólares en tiempo realGit + GitHubControl de versiones

📁 Estructura del proyecto
calculadora_de_gastos/
├── main.py                  # Punto de entrada y menú principal
├── models/
│   └── gasto.py             # Clase Gasto
├── services/
│   └── gastos_services.py   # Lógica de negocio
├── utils/
│   └── menu.py              # Menú de opciones
├── gastos.json              # Datos persistidos (generado automáticamente)
├── requirements.txt         # Dependencias del proyecto
└── .gitignore

⚙️ Instalación
bash# Clonar el repositorio
git clone https://github.com/JorgeLOG123/calculadora_de_gastos.git
cd calculadora_de_gastos

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python main.py

📦 Dependencias

requests — para consumir la API del dólar blue


🌐 API utilizada
DolarAPI — provee el tipo de cambio del dólar blue en Argentina en tiempo real.

📌 Estado del proyecto

🚧 En desarrollo activo — el proyecto crece a medida que aprendo nuevos conceptos de Python.

Próximas funcionalidades

 Eliminar gastos
 Editar gastos existentes
 Filtros por fecha
 Estadísticas por categoría


👨‍💻 Autor
Jorge — @JorgeLOG123
Proyecto de aprendizaje basado en el curso Hello-Python de @mouredev.
