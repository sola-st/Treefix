import numpy as np # pragma: no cover

class MockOps(object):# pragma: no cover
    @staticmethod# pragma: no cover
    def name_scope(name, default_name, values):# pragma: no cover
        return name  # Simplified for mock purposes# pragma: no cover
ops = MockOps() # pragma: no cover
"SparseSoftmax" # pragma: no cover
class MockGenSparseOps(object):# pragma: no cover
    @staticmethod# pragma: no cover
    def sparse_softmax(indices, values, dense_shape):# pragma: no cover
        return tf.nn.softmax(tf.sparse.to_dense(sp_input)).numpy()  # Simplified to return softmax values# pragma: no cover
# pragma: no cover
gen_sparse_ops = MockGenSparseOps() # pragma: no cover
class MockSparseTensor(object):# pragma: no cover
    def __init__(self, indices, values, dense_shape):# pragma: no cover
        self.indices = indices# pragma: no cover
        self.values = values# pragma: no cover
        self.dense_shape = dense_shape# pragma: no cover
sparse_tensor = MockSparseTensor # pragma: no cover

import numpy as np # pragma: no cover

class MockOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def name_scope(name, default_name, inputs):# pragma: no cover
        return name  # For mock purposes # pragma: no cover
ops = MockOps() # pragma: no cover
name = 'sparse_softmax_test' # pragma: no cover
class MockGenSparseOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def sparse_softmax(indices, values, dense_shape):# pragma: no cover
        return tf.nn.softmax(tf.sparse.to_dense(sp_input)).numpy() # pragma: no cover
gen_sparse_ops = MockGenSparseOps() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
from l3.Runtime import _l_
"""Applies softmax to a batched N-D `SparseTensor`.

  The inputs represent an N-D SparseTensor with logical shape `[..., B, C]`
  (where `N >= 2`), and with indices sorted in the canonical lexicographic
  order.

  This op is equivalent to applying the normal `tf.nn.softmax()` to each
  innermost logical submatrix with shape `[B, C]`, but with the catch that *the
  implicitly zero elements do not participate*.  Specifically, the algorithm is
  equivalent to:

    (1) Applies `tf.nn.softmax()` to a densified view of each innermost
        submatrix with shape `[B, C]`, along the size-C dimension;
    (2) Masks out the original implicitly-zero locations;
    (3) Renormalizes the remaining elements.

  Hence, the `SparseTensor` result has exactly the same non-zero indices and
  shape.

  Example using a 3-D SparseTensor:

    >>> st = tf.sparse.from_dense(
    ...   [[[0., np.e],
    ...     [1., 0.]],
    ...
    ...    [[np.e, 0.],
    ...     [np.e, np.e]]])
    >>> res = tf.sparse.softmax(st)
    >>> res.indices
    <tf.Tensor: shape=(5, 3), dtype=int64, numpy=
    array([[0, 0, 1],
           [0, 1, 0],
           [1, 0, 0],
           [1, 1, 0],
           [1, 1, 1]])>
    >>> res.values
    <tf.Tensor: ... numpy=array([1. , 1. , 1. , 0.5, 0.5], dtype=float32)>
    >>> res.dense_shape
    <tf.Tensor: shape=(3,), dtype=int64, numpy=array([2, 2, 2])>
    >>> tf.sparse.to_dense(res)
    <tf.Tensor: shape=(2, 2, 2), dtype=float32, numpy=
    array([[[0. , 1. ],
            [1. , 0. ]],
           [[1. , 0. ],
            [0.5, 0.5]]], dtype=float32)>

  Args:
    sp_input: N-D `SparseTensor`, where `N >= 2`.
    name: optional name of the operation.
  Returns:
    output: N-D `SparseTensor` representing the results.
  """
with ops.name_scope(name, "SparseSoftmax",
                    [sp_input.indices, sp_input.values]) as name:
    _l_(9689)

    out_vals = gen_sparse_ops.sparse_softmax(sp_input.indices, sp_input.values,
                                             sp_input.dense_shape)
    _l_(9687)
    aux = sparse_tensor.SparseTensor(sp_input.indices, out_vals,
                                      sp_input.dense_shape)
    _l_(9688)
    exit(aux)
