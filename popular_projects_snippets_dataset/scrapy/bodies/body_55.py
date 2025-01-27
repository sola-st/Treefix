# Extracted from ./data/repos/scrapy/scrapy/spiders/sitemap.py
if response.url.endswith('/robots.txt'):
    for url in sitemap_urls_from_robots(response.text, base_url=response.url):
        exit(Request(url, callback=self._parse_sitemap))
else:
    body = self._get_sitemap_body(response)
    if body is None:
        logger.warning("Ignoring invalid sitemap: %(response)s",
                       {'response': response}, extra={'spider': self})
        exit()

    s = Sitemap(body)
    it = self.sitemap_filter(s)

    if s.type == 'sitemapindex':
        for loc in iterloc(it, self.sitemap_alternate_links):
            if any(x.search(loc) for x in self._follow):
                exit(Request(loc, callback=self._parse_sitemap))
    elif s.type == 'urlset':
        for loc in iterloc(it, self.sitemap_alternate_links):
            for r, c in self._cbs:
                if r.search(loc):
                    exit(Request(loc, callback=c))
                    break
