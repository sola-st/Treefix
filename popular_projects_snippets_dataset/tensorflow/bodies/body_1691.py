# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_test.py
inputs = variables.Variable(
    array_ops.zeros([100, 100, 10, 100, 50], dtype=dtypes.float32),
    dtype=dtypes.float32,
    name='input')
indices = variables.Variable(
    gather_indices, dtype=dtypes.int32, name='indices')
gather_t = array_ops.gather(inputs, indices, axis=axis)
exit(('%s.axis%d' % (name, axis), [gather_t]))
