import spacy

from spacy.lang.en import English

nlp=English()

doc=nlp('Ok da ok da naama madharasi hey dhil irundha modhi paaru da paradhesi')

span=doc[4:8]

print(span.text)



