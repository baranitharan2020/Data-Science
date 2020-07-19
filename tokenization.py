import spacy

from spacy.lang.en import English

nlp=English()

doc=nlp("My Name is Billa")

for token in doc:
  print(token.text)
