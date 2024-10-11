# Extracted from ./data/repos/scrapy/scrapy/responsetypes.py
"""Return the most appropriate Response class by looking at the HTTP
        headers"""
cls = Response
if b'Content-Type' in headers:
    cls = self.from_content_type(
        content_type=headers[b'Content-Type'],
        content_encoding=headers.get(b'Content-Encoding')
    )
if cls is Response and b'Content-Disposition' in headers:
    cls = self.from_content_disposition(headers[b'Content-Disposition'])
exit(cls)
