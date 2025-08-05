import streamlit as st
import pandas as pd
from openai import OpenAI
import os
from unidecode import unidecode

# === insertar api_key ===
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# === CARGAR CSV con separador ;
df = pd.read_csv("productos.csv", sep=";")
df['precio'] = df['precio'].replace(r'[\$,]', '', regex=True).astype(float)
df['rating'] = df['rating'].astype(int)
df['marca'] = df['marca'].apply(lambda x: unidecode(x.strip().lower()))

# === FUNCIÓN 1: respuestas con CSV
def responder_csv(pregunta):
    pregunta = unidecode(pregunta.lower())

    if any(p in pregunta for p in ["bajo presupuesto", "más barato", "economica", "barata"]):
        p = df.loc[df['precio'].idxmin()]
        return f"💰 Recomiendo el **{p['nombre']}**, cuesta ${p['precio']:.2f} y tiene un rating de {p['rating']}."

    elif any(p in pregunta for p in ["caro", "más caro", "premium"]):
        p = df.loc[df['precio'].idxmax()]
        return f"💎 Recomiendo el **{p['nombre']}**, cuesta ${p['precio']:.2f} y tiene un rating de {p['rating']}."

    elif "calidad-precio" in pregunta or "vale la pena" in pregunta:
        df['calidad_precio'] = df['rating'] / df['precio']
        p = df.loc[df['calidad_precio'].idxmax()]
        return f"⚖️ Mejor calidad-precio: **{p['nombre']}**, ratio {p['calidad_precio']:.2f}."

    elif any(marca in pregunta for marca in df['marca'].unique()):
        for marca in df['marca'].unique():
            if marca in pregunta:
                sub = df[df['marca'] == marca]
                if sub.empty:
                    return f"No encontré productos de la marca **{marca}**."
                return f"La marca **{marca.capitalize()}** tiene {len(sub)} productos con rating promedio de {sub['rating'].mean():.1f} y precio promedio de ${sub['precio'].mean():.2f}."

    return None  # si no encontró nada

# === FUNCIÓN 2: respaldo con OpenAI
def responder_con_gpt(pregunta):
    try:
        catalogo = "\n".join([
            f"{row['nombre']} (${row['precio']:.2f}, rating {row['rating']}, marca {row['marca'].capitalize()})."
            for _, row in df.iterrows()
        ])

        system_prompt = (
            "Eres un asistente experto en laptops. Responde como si estuvieras ayudando a un cliente en un ecommerce.\n"
            "Solo puedes recomendar productos del siguiente catálogo:\n" + catalogo
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": pregunta}
            ],
            temperature=0.6,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error al usar OpenAI: {e}"

# === INTERFAZ CON STREAMLIT
st.title("🛒 Asistente de compras de laptops")
st.markdown("Haz tu pregunta sobre laptops (ej. 'barato', 'premium', 'calidad-precio', o necesidades específicas como 'diseño gráfico')")

pregunta = st.text_input("💬 Tu pregunta:")

if pregunta:
    respuesta = responder_csv(pregunta)
    if respuesta is None:
        respuesta = responder_con_gpt(pregunta)
    st.markdown(f"**🤖 Respuesta:** {respuesta}")

