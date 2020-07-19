import spacy
nlp = spacy.load("en_core_web_sm")

set = nlp("She ate the pizza")

for token in set:

    print(token.text, token.pos_)
