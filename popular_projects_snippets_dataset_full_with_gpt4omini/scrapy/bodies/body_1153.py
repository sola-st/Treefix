# Extracted from ./data/repos/scrapy/scrapy/http/request/json_request.py
dumps_kwargs = copy.deepcopy(dumps_kwargs) if dumps_kwargs is not None else {}
dumps_kwargs.setdefault('sort_keys', True)
self._dumps_kwargs = dumps_kwargs

body_passed = kwargs.get('body', None) is not None
data = kwargs.pop('data', None)
data_passed = data is not None

if body_passed and data_passed:
    warnings.warn('Both body and data passed. data will be ignored')
elif not body_passed and data_passed:
    kwargs['body'] = self._dumps(data)
    if 'method' not in kwargs:
        kwargs['method'] = 'POST'

super().__init__(*args, **kwargs)
self.headers.setdefault('Content-Type', 'application/json')
self.headers.setdefault('Accept', 'application/json, text/javascript, */*; q=0.01')
