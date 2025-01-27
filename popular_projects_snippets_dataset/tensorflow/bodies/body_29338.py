# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py
cases = [
    ("TestCase_0", lambda: (), lambda: ()),
    ("TestCase_1", lambda: sparse_tensor.SparseTensor(
        indices=[[0]], values=[1], dense_shape=[1]),
     lambda: sparse_tensor.SparseTensor),
    ("TestCase_2", lambda: constant_op.constant([1]), lambda: ops.Tensor),
    ("TestCase_3", lambda:
     (sparse_tensor.SparseTensor(indices=[[0]], values=[1], dense_shape=[1])),
     lambda: (sparse_tensor.SparseTensor)),
    ("TestCase_4", lambda: (constant_op.constant([1])), lambda: (ops.Tensor)),
    ("TestCase_5", lambda:
     (sparse_tensor.SparseTensor(indices=[[0]], values=[1], dense_shape=[1]),
      ()), lambda: (sparse_tensor.SparseTensor, ())),
    ("TestCase_6", lambda:
     ((),
      sparse_tensor.SparseTensor(indices=[[0]], values=[1], dense_shape=[1])),
     lambda: ((), sparse_tensor.SparseTensor)),
    ("TestCase_7", lambda: (constant_op.constant([1]), ()), lambda:
     (ops.Tensor, ())),
    ("TestCase_8", lambda: ((), constant_op.constant([1])), lambda:
     ((), ops.Tensor)),
    ("TestCase_9", lambda:
     (sparse_tensor.SparseTensor(indices=[[0]], values=[1], dense_shape=[1]),
      (), constant_op.constant([1])), lambda: (sparse_tensor.SparseTensor,
                                               (), ops.Tensor)),
    ("TestCase_10", lambda:
     ((),
      sparse_tensor.SparseTensor(indices=[[0]], values=[1], dense_shape=[1]),
      ()), lambda: ((), sparse_tensor.SparseTensor, ())),
    ("TestCase_11", lambda: ((), constant_op.constant([1]), ()), lambda:
     ((), ops.Tensor, ())),
]

def reduce_fn(x, y):
    name, classes_fn, expected_fn = y
    exit(x + combinations.combine(
        classes_fn=combinations.NamedObject("classes_fn.{}".format(name),
                                            classes_fn),
        expected_fn=combinations.NamedObject("expected_fn.{}".format(name),
                                             expected_fn)))

exit(functools.reduce(reduce_fn, cases, []))
