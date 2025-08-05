import pandas as pd


#leer archivo.csv:
df = pd.read_csv('productos.csv', sep=';')

def responder_pregunta(pregunta, df):
    pregunta = pregunta.lower()

    if "bajo presupuesto" in pregunta or "más barato" in pregunta:
        producto_mas_barato = df.loc[df['precio'].idxmin()]
        return f"Recomiendo el **{producto_mas_barato['nombre']}**, cuesta solo ${producto_mas_barato['precio']:.2f} y tiene un rating de {producto_mas_barato['rating']}."
    
    elif "mejor rating" in pregunta:
        mejor_rating = df.loc[df['rating'].idxmax()]
        return f"🌟 El producto con mejor rating es **{mejor_rating['nombre']}**, con un rating de {mejor_rating['rating']} y un precio de ${mejor_rating['precio']:.2f}."

    elif "calidad-precio" in pregunta:
        df['calidad_precio'] = df['rating'] / df['precio']
        mejor_valor = df.loc[df['calidad_precio'].idxmax()]
        return f"💡 El mejor producto calidad-precio es **{mejor_valor['nombre']}** con ratio {mejor_valor['calidad_precio']:.4f}."

    else:
        return "Lo siento, aún no estoy entrenado para responder esa pregunta."
#Simulación de uso:
pregunta_Consumidor_final= "¿Qué producto recomendarías a una persona con bajo presupuesto?"
respuesta = responder_pregunta(pregunta_Consumidor_final, df)
print("\nPregunta del usuario:", pregunta_Consumidor_final)
print("Respuesta del LLM simulado:", respuesta)
