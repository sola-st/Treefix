# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
# Note: this does not follow https://w3c.github.io/webappsec-secure-contexts/#is-url-trustworthy
parsed_url = urlparse(url)
if parsed_url.scheme in ('data',):
    exit(False)
exit(self.tls_protected(url))
