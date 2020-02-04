from bs4 import BeautifulSoup
import requests
#input a web page url upon request
url_input = input("Paste url here: ")

def link_lables():
    url = requests.get(url_input)  # Using the input url above request module is using the get function to pull from the website
    src = url.content              
    soup = BeautifulSoup(src, 'lxml')
    links = soup.find_all('a')
    for link in links:
        print(link.text)


link_lables()


