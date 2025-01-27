# Extracted from ./data/repos/scrapy/scrapy/http/request/rpc.py
if 'body' not in kwargs and 'params' in kwargs:
    kw = dict((k, kwargs.pop(k)) for k in DUMPS_ARGS if k in kwargs)
    kwargs['body'] = xmlrpclib.dumps(**kw)

# spec defines that requests must use POST method
kwargs.setdefault('method', 'POST')

# xmlrpc query multiples times over the same url
kwargs.setdefault('dont_filter', True)

# restore encoding
if encoding is not None:
    kwargs['encoding'] = encoding

super().__init__(*args, **kwargs)
self.headers.setdefault('Content-Type', 'text/xml')
