import nltk

from nltk.tokenize import sent_tokenize, word_tokenize

Temp = "Hello Mr.Baranitharan!, How are you? Here we'll discuss about the Tokenization using NLTK. NLTK is a package in python for Natural language processing (NLP)"

print(sent_tokenize(Temp))

print(word_tokenize(Temp))
