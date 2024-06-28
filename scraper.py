# Import necessary libraries
import requests
from bs4 import BeautifulSoup

def get_page_text(url):
    # Use requests to get the content of the page
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract and return the text from the parsed HTML
        return soup.get_text()
    else:
        return f"Failed to retrieve the page. Status code: {response.status_code}"

# Example usage
url = 'https://www.tiktok.com/legal/page/us/privacy-policy/en'
page_text = get_page_text(url)
print(page_text)