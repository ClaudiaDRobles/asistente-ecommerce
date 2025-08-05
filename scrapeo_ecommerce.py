import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    html = respuesta.text

    soup = BeautifulSoup(html, 'html.parser')
    productos = soup.find_all('div', class_='card thumbnail')

    with open('productos.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['nombre', 'marca', 'precio', 'rating'])

        for producto in productos:
            a = producto.find('a', class_='title')
            titulo = a.text.strip() if a else 'sin título'

            precio = producto.find('h4', class_='price')
            precio_producto = precio.text.strip() if precio else 'sin precio'

            rating = producto.find('p', {'data-rating': True})
            rating_value = rating.get('data-rating') if rating else '0'


            marca = titulo.split()[0]
            writer.writerow([titulo, marca, precio_producto, rating_value])

    print("✅ CSV generado correctamente: productos.csv")

else:
    print(f"❌ Error al acceder a la página: {respuesta.status_code}")
