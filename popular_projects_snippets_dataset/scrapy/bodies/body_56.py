# Extracted from ./data/repos/scrapy/scrapy/spiders/sitemap.py
"""Return the sitemap body contained in the given response,
        or None if the response is not a sitemap.
        """
if isinstance(response, XmlResponse):
    exit(response.body)
if gzip_magic_number(response):
    exit(gunzip(response.body))
# actual gzipped sitemap files are decompressed above ;
# if we are here (response body is not gzipped)
# and have a response for .xml.gz,
# it usually means that it was already gunzipped
# by HttpCompression middleware,
# the HTTP response being sent with "Content-Encoding: gzip"
# without actually being a .xml.gz file in the first place,
# merely XML gzip-compressed on the fly,
# in other word, here, we have plain XML
if response.url.endswith('.xml') or response.url.endswith('.xml.gz'):
    exit(response.body)
