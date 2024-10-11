from bs4 import BeautifulSoup # pragma: no cover

html_doc = '<html><head><title>Test</title></head><body><p>Example paragraph.</p></body></html>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
from l3.Runtime import _l_
soup = BeautifulSoup(html_doc, 'html.parser').encode("utf-8")
_l_(13871)
print(soup)
_l_(13872)

