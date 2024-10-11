class MockSparseTensor: pass # pragma: no cover
sparse_tensor = type('Mock', (object,), {'SparseTensor': MockSparseTensor}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
from l3.Runtime import _l_
aux = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]],
    values=constant_op.constant([1, 2], dtype=dtypes.int64),
    dense_shape=[3, 4])
_l_(4366)
exit(aux)
