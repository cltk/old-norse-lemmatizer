# Old Norse lemmatizer

The main aim of this repository is to generate all the forms that Old Norse words can have, given the Zoëga's 
dictionary and the Old Norse inflection rules.

## TODOs

* [x] Retrieve lemmata of the [Zoëga's dictionary](https://github.com/cltk/old_norse_dictionary_zoega).
* [ ] For each lemma, extract the word category (noun, verb, pronoun, article, number, etc). One lemma can represent several word categories. 
* [ ] For a given lemma in a certain word category, extract the precise subcategory: a verbs may be strong, weak or preterite-present, nouns can be strong or weak, masculine, feminine or neuter, etc.
* [ ] For a given lemma with its precise word category, generate all the possible forms that a lemma can have thanks to [Old Norse lemma inflection module of CLTK](https://github.com/cltk/cltk/tree/master/cltk/inflection/old_norse).
* [ ] Compute frequencies of each word forms in Old Norse corpora.
* [ ] Make lemmatizers for Old Norse.
