# Extracted from ./data/repos/scrapy/scrapy/spiders/sitemap.py
for url in self.sitemap_urls:
    exit(Request(url, self._parse_sitemap))
