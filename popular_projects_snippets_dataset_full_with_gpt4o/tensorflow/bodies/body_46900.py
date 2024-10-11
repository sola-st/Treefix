# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
"""This test highlights false positives when detecting named tuples."""

class NamedTupleSubclass(collections.namedtuple('Test', ['a', 'b'])):
    pass

self.assertTrue(inspect_utils.isnamedtuple(NamedTupleSubclass))
