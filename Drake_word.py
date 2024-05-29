from collections import Counter
from pprint import pprint

from Drake_any_song import liste_des_musiques

def filtre(chaine):
    c = 0
    Ctest = False
    Ptest = False
    chaine_filtree = []
    while c < len(chaine):
        if chaine[c] == '[':
            Ctest = True
        if chaine[c] == '(':
            Ptest = True
        temp = chaine[c]
        if not (Ctest or Ptest):
            chaine_filtree.append(temp)
        if temp == ']':
            Ctest = False
        if temp == ')':
            Ptest = False
        c += 1

    return ''.join(chaine_filtree)




def any_music_filtre():
    chemin = liste_des_musiques()[0]
    musiques = liste_des_musiques()[1]
    for musique in musiques:
        with open(chemin / musique,'r',encoding='utf-8') as f:
            r= f.read().replace("]\n",']').replace(")\n",')')
        with open(chemin / musique,'w',encoding='utf-8') as f:
            f.write(filtre(r).replace(",","").replace(".","").replace('\n\n','\n'))

def drake_words():
    chemin = liste_des_musiques()[0]
    musiques = liste_des_musiques()[1]
    words = []
    for musique in musiques:
        with open(chemin / musique,'r',encoding='utf-8') as f:
            r = f.read().replace("]\n",']').replace(")\n",')').replace('\n',' ')
        words.extend(r.split())
    words =[word.lower().strip('.') for word in words if len(word)>4]
    return words

def commun_word(list):
    c = Counter(list)
    return c.most_common(10)

pprint(commun_word(drake_words()))