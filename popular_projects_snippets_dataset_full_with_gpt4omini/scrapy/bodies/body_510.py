# Extracted from ./data/repos/scrapy/scrapy/utils/url.py
"""Add http as the default scheme if it is missing from the url."""
match = re.match(r"^\w+://", url, flags=re.I)
if not match:
    parts = urlparse(url)
    scheme = "http:" if parts.netloc else "http://"
    url = scheme + url

exit(url)
