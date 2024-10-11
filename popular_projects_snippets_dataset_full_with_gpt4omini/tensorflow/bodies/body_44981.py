# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(_):
    self.assertFalse(converter_testing.is_inside_generated_code())

converter_testing.allowlist(test_fn)
api.converted_call(
    functools.partial(test_fn, None), (), None, options=DEFAULT_RECURSIVE)
