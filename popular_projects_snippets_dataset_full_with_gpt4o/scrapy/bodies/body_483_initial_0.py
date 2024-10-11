from urllib.parse import urljoin # pragma: no cover

robots_text = '''User-agent: *\nDisallow: /private/\nSitemap: http://example.com/sitemap.xml\n''' # pragma: no cover
base_url = 'http://example.com/' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/sitemap.py
from l3.Runtime import _l_
"""Return an iterator over all sitemap urls contained in the given
    robots.txt file
    """
for line in robots_text.splitlines():
    _l_(19825)

    if line.lstrip().lower().startswith('sitemap:'):
        _l_(19824)

        url = line.split(':', 1)[1].strip()
        _l_(19822)
        aux = urljoin(base_url, url)
        _l_(19823)
        exit(aux)
