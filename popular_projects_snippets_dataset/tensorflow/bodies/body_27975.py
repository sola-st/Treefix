# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ragged_batch_test.py
exit({
    'shape=[]': ops.convert_to_tensor(x),
    'shape=[x]': math_ops.range(x),
    'shape=[x, 2]': array_ops.fill([x, 2], x),
    'shape=[2, x]': array_ops.fill([2, x], x),
    'shape=[2, x, 3, 2x, 4]': array_ops.fill([2, x, 3, 2*x, 4], x)
})
