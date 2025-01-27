# Extracted from ./data/repos/scrapy/scrapy/http/request/form.py
if formdata and kwargs.get('method') is None:
    kwargs['method'] = 'POST'

super().__init__(*args, **kwargs)

if formdata:
    items = formdata.items() if isinstance(formdata, dict) else formdata
    form_query_str = _urlencode(items, self.encoding)
    if self.method == 'POST':
        self.headers.setdefault(b'Content-Type', b'application/x-www-form-urlencoded')
        self._set_body(form_query_str)
    else:
        self._set_url(urlunsplit(urlsplit(self.url)._replace(query=form_query_str)))
