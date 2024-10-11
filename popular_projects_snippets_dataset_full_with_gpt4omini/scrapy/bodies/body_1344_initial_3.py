import typing # pragma: no cover

tag = '{http://www.w3.org/1999/xhtml}div' # pragma: no cover
XHTML_NAMESPACE = 'http://www.w3.org/1999/xhtml' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
from l3.Runtime import _l_
if isinstance(tag, str):
    _l_(10249)

    if tag[0] == '{' and tag[1:len(XHTML_NAMESPACE) + 1] == XHTML_NAMESPACE:
        _l_(10248)

        aux = tag.split('}')[-1]
        _l_(10247)
        exit(aux)
aux = tag
_l_(10250)
exit(aux)
