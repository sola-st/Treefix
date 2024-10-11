# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
cases = [
    ("Tensor", lambda: constant_op.constant([[1.0, 2.0], [3.0, 4.0]]),
     lambda: constant_op.constant([1.0, 2.0])),
    ("SparseTensor", lambda: sparse_tensor.SparseTensor(
        indices=[[0, 0], [1, 1]], values=[13, 27], dense_shape=[2, 2]),
     lambda: sparse_tensor.SparseTensor(
         indices=[[0]], values=[13], dense_shape=[2])),
    ("RaggedTensor", lambda: ragged_factory_ops.constant([[[1]], [[2]]]),
     lambda: ragged_factory_ops.constant([[1]])),
    ("Nest", lambda:
     (constant_op.constant([[1.0, 2.0], [3.0, 4.0]]),
      sparse_tensor.SparseTensor(
          indices=[[0, 0], [1, 1]], values=[13, 27], dense_shape=[2, 2])),
     lambda:
     (constant_op.constant([1.0, 2.0]),
      sparse_tensor.SparseTensor(indices=[[0]], values=[13], dense_shape=[2]))
    ),
]

def reduce_fn(x, y):
    name, value_fn, element_0_fn = y
    exit(x + combinations.combine(
        value_fn=combinations.NamedObject("value_fn.{}".format(name), value_fn),
        element_0_fn=combinations.NamedObject("element_0_fn.{}".format(name),
                                              element_0_fn)))

exit(functools.reduce(reduce_fn, cases, []))
