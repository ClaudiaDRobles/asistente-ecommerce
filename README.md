<h1 align="left">🛍️ Asistente de Compras de Laptops</h1>

<p align="left">Un asistente conversacional inteligente que recomienda laptops según tus necesidades (diseño gráfico, juegos, trabajo, estudio, etc.), combinando scraping de productos reales, análisis con Pandas y recomendaciones potenciadas por un modelo LLM de OpenAI.</p>

---

  ### 🚀¿Cómo funciona?


### 🛒 Scraping de productos reales  
Se extraen datos desde tiendas online y se guardan en un archivo CSV con información como nombre, precio, marca, uso recomendado, etc.

### 🧹 Limpieza de datos  
Un script (`limpieza.py`) procesa y estandariza los datos con **Pandas**, eliminando inconsistencias.

### 💬 Asistente conversacional  
Una app construida con **Streamlit** (`app.py`) permite que el usuario formule preguntas como:

- “¿Cuál es la mejor laptop para diseño gráfico?”
- “Recomiéndame una laptop buena y barata para estudiar”

### 🧠 Motor de recomendación (LLM)  
El asistente utiliza la **API de OpenAI (GPT)** para interpretar la intención del usuario, filtrar el CSV y generar una recomendación precisa.


---

### 🧠 ¿Qué rol cumple el LLM?

El modelo GPT funciona como cerebro inteligente del asistente:

- Interpreta lenguaje natural del usuario

- Entiende criterios complejos como “calidad-precio” o “para edición de video”

- Compara productos del CSV con lógica contextual

- Genera explicaciones humanas sobre por qué recomienda ciertos modelos

---

### 🛠️ Tecnologías utilizadas

- Python 3.10

- Streamlit (interfaz web)

- Pandas (procesamiento de datos)

- OpenAI API (modelo GPT)

- request y BeautifulSoup (para scraping)

- dotenv (manejo seguro de API keys)


---
### 📦 Cómo ejecutar

# Clonar el repositorio
git clone https://github.com/tu_usuario/asistente-ecommerce.git
cd asistente-ecommerce

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env
touch .env
# Añadir tu clave
echo "OPENAI_API_KEY=sk-..." >> .env

# Ejecutar app
streamlit run app.py


---

### 🧪 Ejemplos de uso

*** Pregunta: ¿Cuál es la mejor laptop para arquitectura? ***
👉 Respuesta: “Te recomiendo la Acer Nitro 5 por su buena tarjeta gráfica, RAM expandible y excelente rendimiento con software como AutoCAD.”

*** Pregunta: ¿Una laptop ligera con buena batería para clases? ***
👉 Respuesta: “La HP Pavilion x360 es una excelente opción por su peso liviano y autonomía de 9 horas.”

