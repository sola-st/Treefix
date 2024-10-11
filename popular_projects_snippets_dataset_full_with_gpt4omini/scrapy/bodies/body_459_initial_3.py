from twisted.web import resource, server, static, util # pragma: no cover
from twisted.web.server import Site # pragma: no cover

class NoMetaRefreshRedirect(util.Redirect): pass # pragma: no cover
resource.Resource = type('MockResource', (object,), {}) # pragma: no cover
static.Data = type('MockStaticData', (object,), {'__init__': lambda self, data, content_type: None}) # pragma: no cover
util.Redirect = type('MockRedirect', (object,), {'__init__': lambda self, url: None}) # pragma: no cover
server.Site = type('MockSite', (object,), {'__init__': lambda self, resource: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
r = resource.Resource()
_l_(9184)
r.putChild(b"text", static.Data(b"Works", "text/plain"))
_l_(9185)
r.putChild(b"html", static.Data(b"<body><p class='one'>Works</p><p class='two'>World</p></body>", "text/html"))
_l_(9186)
r.putChild(b"enc-gb18030", static.Data(b"<p>gb18030 encoding</p>", "text/html; charset=gb18030"))
_l_(9187)
r.putChild(b"redirect", util.Redirect(b"/redirected"))
_l_(9188)
r.putChild(b"redirect-no-meta-refresh", NoMetaRefreshRedirect(b"/redirected"))
_l_(9189)
r.putChild(b"redirected", static.Data(b"Redirected here", "text/plain"))
_l_(9190)
aux = server.Site(r)
_l_(9191)
exit(aux)
