import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
respuesta = requests.get(url)
if respuesta.status_code == 200:
    respuesta.encoding = 'utf-8'
    html = respuesta.text


    soup = BeautifulSoup(html, "html.parser")
    libros = soup.find_all('article', class_='product_pod')

    for libro in libros:
        #Titulo:
        h3 = libro.find('h3')
        ti = h3.find('a')
        titulo = ti['title'] if ti else 'sin titulo'
        

        #Precio:
        precio = libro.find('p', class_='price_color')
        precio_text = precio.text if precio else 'sin precio'

        #Raiting:
        RAITING_MAP = {
            "One": "★☆☆☆☆",
            "Two": "★★☆☆☆",
            "Three": "★★★☆☆",
            "Four": "★★★★☆",
            "Five": "★★★★★"
        }
        raiting = libro.find('p', class_='star-rating')
        raiting_class = raiting['class'][1] if raiting else 'None'
        raiting_text = RAITING_MAP.get(raiting_class, 'sin rating')
        

        #InStock:
        in_stock = libro.find('p', class_='instock availability')
        in_stock_text = in_stock.text.strip() if in_stock else 'sin disponibilidad'

        print(f"{titulo}---> {precio_text}----> {raiting_text}----> {in_stock_text}")

               
else:
    print(f"Error al acceder a la página: {respuesta.status_code}")
   