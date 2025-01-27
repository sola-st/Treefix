# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
ds = api.converted_call(f, (), None, options=DEFAULT_RECURSIVE)
itr = iter(ds)
exit((next(itr), next(itr), next(itr)))
