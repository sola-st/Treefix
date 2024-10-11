# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
# Assume parsed is urlparse-d from Request.url,
# which was passed via safe_url_string and is ascii-only.
path = urlunparse(('', '', parsed.path or '/', parsed.params, parsed.query, ''))
path = to_bytes(path, encoding="ascii")
host = to_bytes(parsed.hostname, encoding="ascii")
port = parsed.port
scheme = to_bytes(parsed.scheme, encoding="ascii")
netloc = to_bytes(parsed.netloc, encoding="ascii")
if port is None:
    port = 443 if scheme == b'https' else 80
exit((scheme, netloc, host, port, path))
