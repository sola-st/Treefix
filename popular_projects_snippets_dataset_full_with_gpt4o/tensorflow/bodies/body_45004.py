# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass(collections.namedtuple('TestNamedtuple', ('a', 'b'))):
    pass

obj = TestClass(5, 2)
# _asdict is a documented method of namedtuple.
x = api.converted_call(obj._asdict, (), None, options=DEFAULT_RECURSIVE)

self.assertDictEqual(x, {'a': 5, 'b': 2})
