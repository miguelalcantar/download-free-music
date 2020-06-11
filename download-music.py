

#Libraries

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import youtube_dl

# Following the algorithm:

# 1. Get all the songs that the user wants to download

def canciones():

	f = open('Canciones.txt', 'r')
	contenido = f.read()
	lista = contenido.split('\n')

	return lista

# 2. Find those songs, one by one, on Youtube and 3., get their Url

def buscar_url(cancion):

    #Setting enviroment
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)

    url = 'https://www.youtube.com/results?search_query='+cancion.replace(' ','+')

    #Get
    driver.get(url)

    #Source page of the get method
    html_doc = driver.page_source

    #lxml
    soup = bs(html_doc,'lxml')

    #Finding elements
    mainContent = soup.find('div',id='content')
    href = mainContent.find('a',id='thumbnail')

    driver.quit()

    
    href_ = str(href)
    i = href_.find('href')
    j = href_[i:].find(' ') + i
    url = href_[i:j]

    return 'http://www.youtube.com' + url.split('"')[1]

#4. Download those songs ;)

def descargar_canciones(url):

	ydl_opts = {
	    'format': 'bestaudio/best',
	    'outtmpl': '~/Music/%(title)s.%(ext)s',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])

if __name__ == "__main__":

	lista_canciones = canciones()

	for i in range(len(lista_canciones)):
		descargar_canciones(buscar_url(lista_canciones[i]))