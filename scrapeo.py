import requests
from bs4 import BeautifulSoup

#Hacer la petición a la página web
url = "https://dockerlabs.es"
respuesta = requests.get(url)

#Verificar que la petición fue exitosa
if respuesta.status_code ==200:
    html = respuesta.text

    #Parsear el contenido HTML
    soup = BeautifulSoup(html, "html.parser")

    #Encontrar todas las citas
    maquinas= soup.find_all('div', onclick=True)

    conteo_maquinas = 1

    #autores = set()


    #for maquina in maquinas:
        #onclick_text = maquina['onclick']
        #nombre_maquina = onclick_text.split("'")[1]
        #autor_maquina = onclick_text.split("'")[7]
        #autores.add(autor_maquina)
    
    #print("Autores encontrados:")
    #for autor in autores:
        #print(autor)

    for maquina in maquinas:
        onclick_text = maquina['onclick']
        nombre_maquina = onclick_text.split("'")[1]
        dificultad_maquina = onclick_text.split("'")[3]
        autor_maquina = onclick_text.split("'")[7]
        
        print(f"{nombre_maquina}--> {dificultad_maquina} --> {autor_maquina}")

else:
    print(f"Error al acceder a la página: {respuesta.status_code}")