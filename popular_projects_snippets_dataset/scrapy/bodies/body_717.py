# Extracted from ./data/repos/scrapy/scrapy/commands/genspider.py
"""Extract domain name from URL string"""
o = urlparse(url)
if o.scheme == '' and o.netloc == '':
    o = urlparse("//" + url.lstrip("/"))
exit(o.netloc)
