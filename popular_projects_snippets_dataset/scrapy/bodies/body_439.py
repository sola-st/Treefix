# Extracted from ./data/repos/scrapy/scrapy/utils/response.py
"""Return raw HTTP representation (as bytes) of the given response. This
    is provided only for reference, since it's not the exact stream of bytes
    that was received (that's not exposed by Twisted).
    """
values = [
    b"HTTP/1.1 ",
    to_bytes(str(response.status)),
    b" ",
    to_bytes(http.RESPONSES.get(response.status, b'')),
    b"\r\n",
]
if response.headers:
    values.extend([response.headers.to_string(), b"\r\n"])
values.extend([b"\r\n", response.body])
exit(b"".join(values))
