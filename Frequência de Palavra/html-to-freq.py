#by Rychard Maciel 

import urllib.request, urllib.error, urllib.parse, frequencia.base as base

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')
text = base.stripTags(html).lower()
#print(text)
fullwordlist = base.stripNonAlphaNum(text)
wordlist = base.removeStopwords (fullwordlist, base.stopwords) 

#stopwords - são palavras que podem ser consideradas irrelevantes para o conjunto de resultados a ser exibido
#em uma busca realizada em uma search engine. Exemplos: as, e, os, de, para, com, sem, foi.

dictionary = base.wordListToFreqDict(wordlist)
sorteddict = base.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))