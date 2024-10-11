# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reverse_ops_test.py
shape = (7, 5, 9, 11)
for revdim in range(-len(shape), len(shape)):
    self._AssertReverseEqual([revdim], shape)
