"""

"""
from zoegas import reader

from cltk.lemmatize import backoff
from eddas import reader as eddas_reader

voeluspaa = eddas_reader.PoeticEddaLemmatizationReader("Völuspá")

voeluspaa.tagged_words()

lemmatizer = backoff.IdentityLemmatizer()
print(lemmatizer.lemmatize(voeluspaa.words()))


dictionary = reader.Dictionary(reader.dictionary_name)

entries = dictionary.get_entries()

segja = dictionary.find("segja")
print(segja.description)
segja = dictionary.find("ár")
print(segja.description)
segja = dictionary.find("sá")
print(segja.description)
segja = dictionary.find("akr")
print(segja.description)
segja = dictionary.find("telja")
print(segja.description)
segja = dictionary.find("mæla")
print(segja.description)
segja = dictionary.find("vaka")
print(segja.description)


class ZoegasLemmatizer:
    """
    The Zoëga's lemmatizer returns all the inflected forms from an entry.
    """
    def __init__(self):
        pass

