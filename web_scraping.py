import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'
#obtengo la pagina a analizar
html_doc = requests.get(url)
#print(html_doc.text)
#parsear la pagina web
soup = BeautifulSoup(html_doc.text, 'html.parser')


titulo_datos = soup.h1.string
print(titulo_datos)

tabla= soup.find('table')

#Obtener las filas de la tabla
filas = tabla.find_all('tr')
nombres = []
apellidos = []
especialidades = []

for fila in filas:
    celdas = fila.find_all('td')
    if len(celdas)>0:
    # print(celdas)
    #     print(celdas[0]
        nombres.append(celdas[2].string)
        apellidos.append(celdas[3].string)
        especialidades.append(celdas[4].string)

print(nombres)
print(apellidos)
print(especialidades)

df = pd.DataFrame({'Nombres':nombres,'Apellidos':apellidos,'especialidades':especialidades})
df.to_csv('citasmd.csv',index=False, encoding='utf-8')



