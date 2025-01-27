# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py

cases = [
    ("TestCase_0", lambda: (), lambda: (), lambda: ()),
    ("TestCase_1", lambda: tensor_shape.TensorShape([]), lambda: ops.Tensor,
     lambda: tensor_shape.TensorShape([])),
    (
        "TestCase_2",
        lambda: tensor_shape.TensorShape([]),
        lambda: sparse_tensor.SparseTensor,
        lambda: tensor_shape.unknown_shape()  # pylint: disable=unnecessary-lambda
    ),
    ("TestCase_3", lambda: (tensor_shape.TensorShape([])), lambda:
     (ops.Tensor), lambda: (tensor_shape.TensorShape([]))),
    (
        "TestCase_4",
        lambda: (tensor_shape.TensorShape([])),
        lambda: (sparse_tensor.SparseTensor),
        lambda: (tensor_shape.unknown_shape())  # pylint: disable=unnecessary-lambda
    ),
    ("TestCase_5", lambda: (tensor_shape.TensorShape([]), ()), lambda:
     (ops.Tensor, ()), lambda: (tensor_shape.TensorShape([]), ())),
    ("TestCase_6", lambda: ((), tensor_shape.TensorShape([])), lambda:
     ((), ops.Tensor), lambda: ((), tensor_shape.TensorShape([]))),
    ("TestCase_7", lambda: (tensor_shape.TensorShape([]), ()), lambda:
     (sparse_tensor.SparseTensor, ()), lambda: (tensor_shape.unknown_shape(),
                                                ())),
    ("TestCase_8", lambda: ((), tensor_shape.TensorShape([])), lambda:
     ((), sparse_tensor.SparseTensor), lambda: (
         (), tensor_shape.unknown_shape())),
    ("TestCase_9", lambda: (tensor_shape.TensorShape([]),
                            (), tensor_shape.TensorShape([])), lambda:
     (ops.Tensor, (), ops.Tensor), lambda:
     (tensor_shape.TensorShape([]), (), tensor_shape.TensorShape([]))),
    ("TestCase_10", lambda: (tensor_shape.TensorShape([]),
                             (), tensor_shape.TensorShape([])), lambda:
     (sparse_tensor.SparseTensor, (), sparse_tensor.SparseTensor), lambda:
     (tensor_shape.unknown_shape(), (), tensor_shape.unknown_shape())),
    ("TestCase_11", lambda: ((), tensor_shape.TensorShape([]), ()), lambda:
     ((), ops.Tensor, ()), lambda: ((), tensor_shape.TensorShape([]), ())),
    ("TestCase_12", lambda: ((), tensor_shape.TensorShape([]), ()), lambda:
     ((), sparse_tensor.SparseTensor,
      ()), lambda: ((), tensor_shape.unknown_shape(), ()))
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
