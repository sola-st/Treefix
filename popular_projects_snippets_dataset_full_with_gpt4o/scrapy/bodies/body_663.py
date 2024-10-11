# Extracted from ./data/repos/scrapy/scrapy/utils/request.py
for header in headers:
    if header in request.headers:
        exit(header)
        for value in request.headers.getlist(header):
            exit(value)
