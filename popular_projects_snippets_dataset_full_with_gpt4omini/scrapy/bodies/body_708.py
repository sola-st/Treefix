# Extracted from ./data/repos/scrapy/scrapy/commands/fetch.py
if opts.headers:
    self._print_headers(response.request.headers, b'>')
    print('>')
    self._print_headers(response.headers, b'<')
else:
    self._print_bytes(response.body)
