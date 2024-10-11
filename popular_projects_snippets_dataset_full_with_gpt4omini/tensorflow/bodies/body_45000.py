# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

x = api.converted_call(
    collections.namedtuple, ('TestNamedtuple', ('a', 'b')),
    None,
    options=DEFAULT_RECURSIVE)

self.assertTrue(inspect_utils.isnamedtuple(x))
