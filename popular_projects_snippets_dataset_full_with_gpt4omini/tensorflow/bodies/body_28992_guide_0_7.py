constant_op = type('Mock', (object,), {})() # pragma: no cover
constant_op.constant = staticmethod(lambda value, dtype: tf.constant(value, dtype=dtype)) # pragma: no cover
dtypes = type('Mock', (object,), {})() # pragma: no cover
sparse_tensor = type('Mock', (object,), {})() # pragma: no cover
sparse_tensor.SparseTensor = staticmethod(lambda indices, values, dense_shape: tf.sparse.SparseTensor(indices, values, dense_shape)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
from l3.Runtime import _l_
aux = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]],
    values=constant_op.constant([1, 2], dtype=dtypes.int64),
    dense_shape=[3, 4])
_l_(4366)
exit(aux)
