from haystack import component, Document
from typing import List

@component
class Text2Doc:
	@component.output_types(document=List[Document])
	def run(self, text: List[str]):
		return {"document": [Document(content=" ".join(text))]}