# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcompression.py
request.headers.setdefault('Accept-Encoding',
                           b", ".join(ACCEPTED_ENCODINGS))
