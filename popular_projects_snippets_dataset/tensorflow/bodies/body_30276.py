# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
# Random dims of rank 5
shape = np.random.randint(1, 5, size=5)
split_dim = np.random.randint(-5, 5)
if large_num_splits:
    num_split = np.random.randint(16, 25)
else:
    num_split = np.random.randint(2, 8)
size_splits = np.random.randint(2, 8, num_split, dtype=np.int32)
shape[split_dim] = np.sum(size_splits)
inp = self._makeData(shape, dtype)
with test_util.device(use_gpu=True):
    result = self.evaluate(array_ops.split(inp, size_splits, split_dim))
slices = [slice(0, x) for x in shape]
offset = 0
for i in range(num_split):
    slices[split_dim] = slice(offset, offset + size_splits[i])
    offset += size_splits[i]
    self.assertAllEqual(result[i], inp[tuple(slices)])
