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
