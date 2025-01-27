# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
inputs = array_ops.ones((1, 1, 1, 1))
filters = array_ops.ones((1, 1, 1, 1))

def fn():
    nn_ops.convolution_v2(inputs, filters)

self._run(fn, 10000)
