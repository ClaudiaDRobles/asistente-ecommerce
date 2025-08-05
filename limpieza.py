import pandas as pd
import openai
import os
from openai import OpenAI


# === 1. CONFIGURA TU API KEY ===
client = OpenAI(api_key="TU_API_KEY_AQUI")

# Cargar y preparar datos / limpieza de datos
df = pd.read_csv('productos.csv', sep=';')
df['precio'] = df['precio'].replace(r'[\$,]', '', regex=True).astype(float)
df['rating'] = df['rating'].astype(int)
df['marca'] = df['marca'].str.strip().str.lower()

# Función de respuesta
def responder_pregunta(pregunta, df):
    pregunta = pregunta.lower()
    if("bajo presupuesto" in pregunta 
       or "más barato" in pregunta
       or "económica" in pregunta
       or "barata" in pregunta):
        p_barato = df.loc[df['precio'].idxmin()]
        return f"Recomiendo el **{p_barato['nombre']}**, cuesta solo ${p_barato['precio']:.2f} y tiene un rating de {p_barato['rating']}."
    
    elif("buen presupuesto" in pregunta 
        or "más caro" in pregunta
        or "caro" in pregunta
        or "premium" in pregunta):
        p_caro = df.loc[df['precio'].idxmax()]
        return f"Recomiendo el **{p_caro['nombre']}**, cuesta solo ${p_caro['precio']:.2f} y tiene un rating de {p_caro['rating']}."

    elif("mejor rating" in pregunta 
         or "peor rating" in pregunta
         or "por su calificación" in pregunta
         or "recomiendas" in pregunta):
        p_rating = df.loc[df['rating'].idxmax()]
        return f"El producto con mejor rating es **{p_rating['nombre']}**, con un rating de {p_rating['rating']} y un precio de ${p_rating['precio']:.2f}."

    elif("calidad-precio" in pregunta
        or "vale la pena" in pregunta
        or "relacion calidad" in pregunta):
        df['calidad_precio'] = df['rating'] / df['precio']
        p_calidad = df.loc[df['calidad_precio'].idxmax()]
        return f"El mejor producto calidad-precio es **{p_calidad['nombre']}** con ratio {p_calidad['calidad_precio']:.4f}."
    
    elif any(marca.lower() in pregunta for marca in df['marca'].unique()):
        for marca in df['marca'].unique():
            if marca.lower() in pregunta:
                df_marca = df[df['marca'].str.lower() == marca.lower()]
                if not df_marca.empty:
                    promedio_rating = df_marca['rating'].mean()
                    promedio_precio = df_marca['precio'].mean()
                    return f"La marca **{marca}** tiene {len(df_marca)} productos, con un rating promedio de {promedio_rating:.1f} y un precio promedio de ${promedio_precio:.2f}."
        return "No encontré productos de esa marca en la base de datos."

    return None
# === 4. FUNCIÓN GPT PARA CASOS QUE NO COMPRENDE ===
def responder_con_gpt(pregunta):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente de compras experto en laptops. Responde de forma útil, concreta y profesional. Usa los datos del CSV cuando sea posible."},
                {"role": "user", "content": pregunta}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"❌ Error al usar OpenAI: {e}"
    
# Chatbot
historial = []
print("\nHola, soy un asistente virtual. ¿Pregúntame algo sobre algún producto de tu interés?")
print("Escribe 'salir' para terminar la conversación.\n")

while True:
    pregunta_usuario = input("Tú: ")
    if pregunta_usuario.lower() in ['salir', 'exit', 'quit']:
        print("Chat Finalizado. ¡Gracias por usar el asistente!")
        break
    elif pregunta_usuario.lower() == "historial":
        print("\nHistorial de preguntas:")
        for i, (q, r) in enumerate(historial, 1):
            print(f"{i}. Tú: {q}")
            print(f"   🤖 Asistente: {r}")
        continue
    else:
        respuesta = responder_pregunta(pregunta_usuario, df)
        if respuesta is None:
            respuesta = responder_con_gpt(pregunta_usuario)
        historial.append((pregunta_usuario, respuesta))
        print("Asistente:", respuesta)
