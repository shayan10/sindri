import spacy

from haystack import component
from typing import List

nlp = spacy.load("en_core_web_sm")

@component
class Lemmatizer:
   @component.output_types(text=List[str])
   def run(self, text: List[str]):
      docs = nlp.pipe(text)
      result = []
      for doc in docs:
         result.append(" ".join([token.lemma_ for token in doc]))
      return {"text": result}