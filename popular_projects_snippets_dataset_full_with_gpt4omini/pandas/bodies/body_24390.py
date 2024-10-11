# Extracted from ./data/repos/pandas/pandas/io/html.py
from bs4 import BeautifulSoup

bdoc = self._setup_build_doc()
if isinstance(bdoc, bytes) and self.encoding is not None:
    udoc = bdoc.decode(self.encoding)
    from_encoding = None
else:
    udoc = bdoc
    from_encoding = self.encoding

soup = BeautifulSoup(udoc, features="html5lib", from_encoding=from_encoding)

for br in soup.find_all("br"):
    br.replace_with("\n" + br.text)

exit(soup)
