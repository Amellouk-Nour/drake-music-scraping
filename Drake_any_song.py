import requests
import json
from bs4 import BeautifulSoup
from pathlib import Path
from pprint import pprint


#créer la fonction qui me permer de chercher la nieme requete
def get_nieme_urls(n: int):
    return requests.get(f"https://genius.com/api/artists/130/songs?page={n}&sort=popularity")
def sort_Drake_music():
    Drake_links=[]
    for link in links:
        if link.startswith('https://genius.com/Drake') :
            Drake_links.append(link)
    return Drake_links
def extract_lyrics(urls):
    for i in range(len(urls)):
        r=requests.get(urls[i])
        if r.status_code == 200 :
            soup = BeautifulSoup(r.content, 'html.parser')

            name_song = list(soup.find('span',class_='SongHeaderdesktop__HiddenMask-sc-1effuo1-11 iMpFIj').stripped_strings)[0].replace(" /", "").replace("?","").replace("*","").replace("/"," ").replace(':','')

            lyrics_list = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-5 Dzxov')


            chemin = Path.cwd() / 'mes musiques'
            chemin.mkdir(exist_ok=True)

            test = False
            for lyrics in lyrics_list:
                if  list(lyrics.stripped_strings):
                    if list(lyrics.stripped_strings)[0][0] == '[' :
                        test = True
                        (chemin / f'{name_song}.txt').touch()

                        for sentence in lyrics.stripped_strings:
                            for ligne in sentence.splitlines():
                                with (chemin / f'{name_song}.txt').open(mode='a',encoding='utf-8') as fichier:
                                    fichier.write(ligne + '\n')
            if test == True:
                print(f"la musique {name_song} à été enregistrer {i+1}")
        else:
            print(f"la {i} url n'a pas pu être lu")


def get_all_urls():

    if get_nieme_urls(1).status_code == 200 :
        stock = get_nieme_urls(1).json()
        print(f"j'ai importer les données pour la {1} fois")
        del stock["response"]["next_page"]

        for i in range(2,77):
            if get_nieme_urls(i).status_code != 200:
                print("nous n'avons pas pu recuperere l'url")
            else:
                stock["response"]['songs'].extend(get_nieme_urls(i).json()["response"]["songs"])
                print(f"j'ai importer les données pour la {i} fois")
        return stock
    else:
        print("impossible d'initialiser le procésuss")

def liste_des_musiques():
    chemin = Path.cwd() / 'mes musiques'
    return (chemin, [f.name for f in chemin.iterdir() if f.is_file()])


if __name__ == '__main__' :
    with open('links.json','r',encoding='utf-8') as f:
        links =json.load(f)
    extract_lyrics(sort_Drake_music(links))