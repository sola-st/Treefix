# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpproxy.py
if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
    raise NotConfigured
auth_encoding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING')
exit(cls(auth_encoding))
