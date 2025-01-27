# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
input_shape = [1, 64, 32768]
x = np.linspace(
    start=1,
    stop=np.prod(input_shape),
    num=np.prod(input_shape),
    dtype=np.float32).reshape(input_shape)
split_axis = 1
size_splits = [1] * input_shape[split_axis]

y = array_ops.split(x, num_or_size_splits=size_splits, axis=split_axis)

for i in range(input_shape[split_axis]):
    result = y[i]
    expected = x[:, i:i + 1, :]
    self.assertAllEqual(result, expected)
