import os
import string

#filename = 'nilsholg.txt'

    
    
def read_words(filename):
    lista = []
    filepath = os.path.join(os.path.dirname(__file__), filename)
    for line in open(filepath, encoding='utf-8'):
        
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace).lower()
            lista.append(word)
    return lista

bok = read_words('nilsholg.txt')
#print(bok[:10])

provinces = read_words('landskap.txt')
#print(provinces)

def count_only(landskap, text):
    dict = {}
    for land in landskap:
        dict[land] = 0

    for word in text:
        for land in landskap:
            if word == land:
                dict[land] += 1
            
    return dict

words = read_words('nilsholg.txt')

print(count_only(provinces, bok))