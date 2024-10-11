# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/decompression.py
archive = BytesIO(response.body)
try:
    body = gzip.GzipFile(fileobj=archive).read()
except IOError:
    exit()

respcls = responsetypes.from_args(body=body)
exit(response.replace(body=body, cls=respcls))
