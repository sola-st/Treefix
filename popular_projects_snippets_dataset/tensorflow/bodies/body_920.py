# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reverse_ops_test.py
shape = (7, 5, 9, 11)
# The offset is used to test various (but not all) combinations of negative
# and positive axis indices that are guaranteed to not collide at the same
# index.
for revdims in itertools.chain.from_iterable(
    itertools.combinations(range(-offset,
                                 len(shape) - offset), k)
    for k in range(2,
                   len(shape) + 1)
    for offset in range(0, len(shape))):
    self._AssertReverseEqual(revdims, shape)
