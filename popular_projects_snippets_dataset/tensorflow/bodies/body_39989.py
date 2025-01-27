# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
# A `TensorShape` is created the first time `EagerTensor.shape` is
# called, which puts `TensorShape.__init__` on the hotpath. The
# `TensorShape` is created from `EagerTensor._shape_tuple`.

x = array_ops.ones((1, 1))
shape_tuple = x._shape_tuple()

def fn():
    tensor_shape.TensorShape(shape_tuple)

self._run(fn, 100000)
