# Extracted from ./data/repos/scrapy/scrapy/utils/request.py
"""Authenticate the given request (in place) using the HTTP basic access
    authentication mechanism (RFC 2617) and the given username and password
    """
request.headers['Authorization'] = basic_auth_header(username, password)
