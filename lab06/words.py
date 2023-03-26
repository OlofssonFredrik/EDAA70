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
#
#words = read_words('nilsholg.txt')
#
#print(count_only(provinces, bok))
undantag = read_words('undantagsord.txt')

def count_all_except(untantag, text):
    lista = {}
    
    for word in text:
        if word not in undantag:
            if not lista.get(f"{word}"):
                lista[word] = 0
            lista[word] += 1
            
    sorted_dict = dict(sorted(lista.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_dict

scaled_down = dict(list(count_all_except(undantag,bok).items()))
#print(scaled_down)

def filter_list(dict, n):
    new_dict = {}
    for k,v in dict.items():
        if v > n:
            new_dict[k] = v
    
    return new_dict

print(filter_list(scaled_down,100))
        

            
    
    
    