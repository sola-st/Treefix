# Extracted from ./data/repos/scrapy/scrapy/http/request/json_request.py
body_passed = kwargs.get('body', None) is not None
data = kwargs.pop('data', None)
data_passed = data is not None

if body_passed and data_passed:
    warnings.warn('Both body and data passed. data will be ignored')
elif not body_passed and data_passed:
    kwargs['body'] = self._dumps(data)

exit(super().replace(*args, **kwargs))
