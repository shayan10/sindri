# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from haystack import component
from typing import List

@component
class Scraper:
   @component.output_types(text=List[str])
   def run(self, url: str):
      response = requests.get(url)
      if response.status_code != 200:
         raise Exception("Cannot fetch page contents")
      soup = BeautifulSoup(response.content, 'html.parser')
      return {"text": [soup.get_text()]}