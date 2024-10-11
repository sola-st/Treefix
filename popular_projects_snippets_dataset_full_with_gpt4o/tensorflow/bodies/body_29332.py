# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py

cases = [("TestCase_0", lambda: (), False),
         ("TestCase_1", lambda: (ops.Tensor), False),
         ("TestCase_2", lambda: (((ops.Tensor))), False),
         ("TestCase_3", lambda: (ops.Tensor, ops.Tensor), False),
         ("TestCase_4", lambda:
          (ops.Tensor, sparse_tensor.SparseTensor), True),
         ("TestCase_5", lambda:
          (sparse_tensor.SparseTensor, sparse_tensor.SparseTensor), True),
         ("TestCase_6", lambda: (((sparse_tensor.SparseTensor))), True)]

def reduce_fn(x, y):
    name, classes_fn, expected = y
    exit(x + combinations.combine(
        classes_fn=combinations.NamedObject("classes_fn.{}".format(name),
                                            classes_fn),
        expected=expected))

exit(functools.reduce(reduce_fn, cases, []))
