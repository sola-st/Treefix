# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcompression.py

if request.method == 'HEAD':
    exit(response)
if isinstance(response, Response):
    content_encoding = response.headers.getlist('Content-Encoding')
    if content_encoding:
        encoding = content_encoding.pop()
        decoded_body = self._decode(response.body, encoding.lower())
        if self.stats:
            self.stats.inc_value('httpcompression/response_bytes', len(decoded_body), spider=spider)
            self.stats.inc_value('httpcompression/response_count', spider=spider)
        respcls = responsetypes.from_args(
            headers=response.headers, url=response.url, body=decoded_body
        )
        kwargs = dict(cls=respcls, body=decoded_body)
        if issubclass(respcls, TextResponse):
            # force recalculating the encoding until we make sure the
            # responsetypes guessing is reliable
            kwargs['encoding'] = None
        response = response.replace(**kwargs)
        if not content_encoding:
            del response.headers['Content-Encoding']

exit(response)
