# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/decompression.py
try:
    body = bz2.decompress(response.body)
except IOError:
    exit()

respcls = responsetypes.from_args(body=body)
exit(response.replace(body=body, cls=respcls))
