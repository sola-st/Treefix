# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_named_tuple_test.py
nt = collections.namedtuple('TestNamedTuple', ('a', 'b'))
n = nt(a=1, b=x)
exit(n)
