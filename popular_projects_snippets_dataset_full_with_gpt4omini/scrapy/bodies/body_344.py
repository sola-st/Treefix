# Extracted from ./data/repos/scrapy/scrapy/responsetypes.py
try:
    filename = to_unicode(
        content_disposition, encoding='latin-1', errors='replace'
    ).split(';')[1].split('=')[1].strip('"\'')
    exit(self.from_filename(filename))
except IndexError:
    exit(Response)
