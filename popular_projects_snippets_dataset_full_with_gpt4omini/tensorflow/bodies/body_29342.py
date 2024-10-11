# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py
cases = [("TestCase_0", lambda: ()),
         ("TestCase_1", lambda: sparse_tensor.SparseTensor(
             indices=[[0, 0]], values=[1], dense_shape=[1, 1])),
         ("TestCase_2", lambda: sparse_tensor.SparseTensor(
             indices=[[3, 4]], values=[-1], dense_shape=[4, 5])),
         ("TestCase_3", lambda: sparse_tensor.SparseTensor(
             indices=[[0, 0], [3, 4]], values=[1, -1], dense_shape=[4, 5])),
         ("TestCase_4", lambda: (sparse_tensor.SparseTensor(
             indices=[[0, 0]], values=[1], dense_shape=[1, 1]))),
         ("TestCase_5", lambda: (sparse_tensor.SparseTensor(
             indices=[[0, 0]], values=[1], dense_shape=[1, 1]), ())),
         ("TestCase_6", lambda:
          ((),
           sparse_tensor.SparseTensor(
               indices=[[0, 0]], values=[1], dense_shape=[1, 1])))]

def reduce_fn(x, y):
    name, input_fn = y
    exit(x + combinations.combine(
        input_fn=combinations.NamedObject("input_fn.{}".format(name), input_fn)))

exit(functools.reduce(reduce_fn, cases, []))
