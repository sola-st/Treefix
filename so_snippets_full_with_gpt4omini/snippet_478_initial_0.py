from bs4 import BeautifulSoup # pragma: no cover
import requests # pragma: no cover

response = requests.get('http://example.com') # pragma: no cover
soup = BeautifulSoup(response.text, 'html.parser') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class
from l3.Runtime import _l_
soup.find_all("html_element", class_="your_class_name")
_l_(2681)

