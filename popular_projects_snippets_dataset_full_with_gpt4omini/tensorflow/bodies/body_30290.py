# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
# Random dims of rank 5
shape = np.random.randint(0, 5, size=5)
split_dim = np.random.randint(-5, 5)
if large_num_splits:
    num_split = np.random.randint(9, 15)
else:
    num_split = np.random.randint(2, 8)
shape[split_dim] = np.random.randint(2, 5) * num_split
inp = self._makeData(shape, dtype)
with test_util.device(use_gpu=True):
    result = self.evaluate(
        array_ops.split(
            value=inp, num_or_size_splits=num_split, axis=split_dim))
slices = [slice(0, x) for x in shape]
offset = 0
length = shape[split_dim] // num_split
for i in range(num_split):
    slices[split_dim] = slice(offset, offset + length)
    offset += length
    self.assertAllEqual(result[i], inp[tuple(slices)])
