# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
r"""
    Return binary content of a CONNECT request.

    >>> from scrapy.utils.python import to_unicode as s
    >>> s(tunnel_request_data("example.com", 8080))
    'CONNECT example.com:8080 HTTP/1.1\r\nHost: example.com:8080\r\n\r\n'
    >>> s(tunnel_request_data("example.com", 8080, b"123"))
    'CONNECT example.com:8080 HTTP/1.1\r\nHost: example.com:8080\r\nProxy-Authorization: 123\r\n\r\n'
    >>> s(tunnel_request_data(b"example.com", "8090"))
    'CONNECT example.com:8090 HTTP/1.1\r\nHost: example.com:8090\r\n\r\n'
    """
host_value = to_bytes(host, encoding='ascii') + b':' + to_bytes(str(port))
tunnel_req = b'CONNECT ' + host_value + b' HTTP/1.1\r\n'
tunnel_req += b'Host: ' + host_value + b'\r\n'
if proxy_auth_header:
    tunnel_req += b'Proxy-Authorization: ' + proxy_auth_header + b'\r\n'
tunnel_req += b'\r\n'
exit(tunnel_req)
