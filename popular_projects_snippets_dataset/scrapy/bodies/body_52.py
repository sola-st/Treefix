# Extracted from ./data/repos/scrapy/scrapy/spiders/sitemap.py
super().__init__(*a, **kw)
self._cbs = []
for r, c in self.sitemap_rules:
    if isinstance(c, str):
        c = getattr(self, c)
    self._cbs.append((regex(r), c))
self._follow = [regex(x) for x in self.sitemap_follow]
