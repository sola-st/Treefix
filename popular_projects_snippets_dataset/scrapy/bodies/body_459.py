# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
r = resource.Resource()
_l_(20674)
r.putChild(b"text", static.Data(b"Works", "text/plain"))
_l_(20675)
r.putChild(b"html", static.Data(b"<body><p class='one'>Works</p><p class='two'>World</p></body>", "text/html"))
_l_(20676)
r.putChild(b"enc-gb18030", static.Data(b"<p>gb18030 encoding</p>", "text/html; charset=gb18030"))
_l_(20677)
r.putChild(b"redirect", util.Redirect(b"/redirected"))
_l_(20678)
r.putChild(b"redirect-no-meta-refresh", NoMetaRefreshRedirect(b"/redirected"))
_l_(20679)
r.putChild(b"redirected", static.Data(b"Redirected here", "text/plain"))
_l_(20680)
aux = server.Site(r)
_l_(20681)
exit(aux)
