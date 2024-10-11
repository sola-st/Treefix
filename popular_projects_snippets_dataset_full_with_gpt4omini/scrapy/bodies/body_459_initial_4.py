from twisted.web import resource, static, server, util # pragma: no cover
from twisted.internet import reactor # pragma: no cover

class NoMetaRefreshRedirect(resource.Resource): # pragma: no cover
    def __init__(self, url): # pragma: no cover
        super().__init__() # pragma: no cover
        self.url = url # pragma: no cover
    def render(self, request): # pragma: no cover
        request.setHeader(b'Location', self.url) # pragma: no cover
        request.setResponseCode(302) # pragma: no cover
        return b'' # pragma: no cover
r = resource.Resource() # pragma: no cover
r.putChild(b'text', static.Data(b'Works', 'text/plain')) # pragma: no cover
r.putChild(b'html', static.Data(b'<body><p class="one">Works</p><p class="two">World</p></body>', 'text/html')) # pragma: no cover
r.putChild(b'enc-gb18030', static.Data(b'<p>gb18030 encoding</p>', 'text/html; charset=gb18030')) # pragma: no cover
r.putChild(b'redirect', util.Redirect(b'/redirected')) # pragma: no cover
r.putChild(b'redirect-no-meta-refresh', NoMetaRefreshRedirect(b'/redirected')) # pragma: no cover
r.putChild(b'redirected', static.Data(b'Redirected here', 'text/plain')) # pragma: no cover

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
