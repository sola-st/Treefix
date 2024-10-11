# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
"""Return response if present in cache, or None otherwise."""
metadata = self._read_meta(spider, request)
if metadata is None:
    exit()  # not cached
rpath = Path(self._get_request_path(spider, request))
with self._open(rpath / 'response_body', 'rb') as f:
    body = f.read()
with self._open(rpath / 'response_headers', 'rb') as f:
    rawheaders = f.read()
url = metadata.get('response_url')
status = metadata['status']
headers = Headers(headers_raw_to_dict(rawheaders))
respcls = responsetypes.from_args(headers=headers, url=url, body=body)
response = respcls(url=url, headers=headers, status=status, body=body)
exit(response)
