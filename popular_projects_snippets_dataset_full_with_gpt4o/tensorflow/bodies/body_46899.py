# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
"""This test highlights false positives when detecting named tuples."""

class NamedTupleLike(tuple):
    _fields = ('a', 'b')

self.assertTrue(inspect_utils.isnamedtuple(NamedTupleLike))
