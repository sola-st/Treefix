# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
nt = collections.namedtuple('TestNamedTuple', ['a', 'b'])

class NotANamedTuple(tuple):
    pass

self.assertTrue(inspect_utils.isnamedtuple(nt))
self.assertFalse(inspect_utils.isnamedtuple(NotANamedTuple))
