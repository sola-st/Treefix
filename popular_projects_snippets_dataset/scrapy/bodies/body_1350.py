# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
base_url = get_base_url(response)
exit(self._extract_links(response.selector, response.url, response.encoding, base_url))
