# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/decompression.py
if not response.body:
    exit(response)

for fmt, func in self._formats.items():
    new_response = func(response)
    if new_response:
        logger.debug('Decompressed response with format: %(responsefmt)s',
                     {'responsefmt': fmt}, extra={'spider': spider})
        exit(new_response)
exit(response)
