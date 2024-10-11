# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py
cases = [
    ("TestCase_0", lambda: (), lambda: (), lambda: ()),
    ("TestCase_1", lambda: dtypes.int32, lambda: ops.Tensor,
     lambda: dtypes.int32),
    ("TestCase_2", lambda: dtypes.int32, lambda: sparse_tensor.SparseTensor,
     lambda: dtypes.variant),
    ("TestCase_3", lambda: (dtypes.int32), lambda: (ops.Tensor), lambda:
     (dtypes.int32)),
    ("TestCase_4", lambda: (dtypes.int32), lambda:
     (sparse_tensor.SparseTensor), lambda: (dtypes.variant)),
    ("TestCase_5", lambda: (dtypes.int32, ()), lambda:
     (ops.Tensor, ()), lambda: (dtypes.int32, ())),
    ("TestCase_6", lambda: ((), dtypes.int32), lambda:
     ((), ops.Tensor), lambda: ((), dtypes.int32)),
    ("TestCase_7", lambda: (dtypes.int32, ()), lambda:
     (sparse_tensor.SparseTensor, ()), lambda: (dtypes.variant, ())),
    ("TestCase_8", lambda: ((), dtypes.int32), lambda:
     ((), sparse_tensor.SparseTensor), lambda: ((), dtypes.variant)),
    ("TestCase_9", lambda: (dtypes.int32, (), dtypes.int32), lambda:
     (ops.Tensor, (), ops.Tensor), lambda: (dtypes.int32, (), dtypes.int32)),
    ("TestCase_10", lambda: (dtypes.int32, (), dtypes.int32), lambda:
     (sparse_tensor.SparseTensor, (), sparse_tensor.SparseTensor), lambda:
     (dtypes.variant, (), dtypes.variant)),
    ("TestCase_11", lambda: ((), dtypes.int32, ()), lambda:
     ((), ops.Tensor, ()), lambda: ((), dtypes.int32, ())),
    ("TestCase_12", lambda: ((), dtypes.int32, ()), lambda:
     ((), sparse_tensor.SparseTensor, ()), lambda: ((), dtypes.variant, ())),
]

def reduce_fn(x, y):
    name, types_fn, classes_fn, expected_fn = y
    exit(x + combinations.combine(
        types_fn=combinations.NamedObject("types_fn.{}".format(name), types_fn),
        classes_fn=combinations.NamedObject("classes_fn.{}".format(name),
                                            classes_fn),
        expected_fn=combinations.NamedObject("expected_fn.{}".format(name),
                                             expected_fn)))

exit(functools.reduce(reduce_fn, cases, []))
