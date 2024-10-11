# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
input_shape = [1, 64, 32768]
x = np.linspace(start=1,
                stop=np.prod(input_shape),
                num=np.prod(input_shape),
                dtype=np.float32).reshape(input_shape)
split_axis = 1
size_splits = [32, 16, 8, 4, 2, 1, 1]

y = array_ops.split(x, num_or_size_splits=size_splits, axis=split_axis)

start = 0
for i in range(len(size_splits)):
    result = y[i]
    split_size = size_splits[i]
    expected = x[:, start:start+split_size, :]
    start += split_size
    self.assertAllEqual(result, expected)
