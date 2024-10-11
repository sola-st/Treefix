# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/ftp.py
self.__filename = filename
self.body = open(filename, "wb") if filename else BytesIO()
self.size = 0
