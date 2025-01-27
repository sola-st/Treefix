# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
num_split = 1000
size_splits = np.random.randint(1, 3, num_split, dtype=np.int32)
shape = [3, np.sum(size_splits)]
split_dim = 1
inp = self._makeData(shape, dtype)
with test_util.device(use_gpu=True):
    result = self.evaluate(array_ops.split(inp, size_splits, split_dim))
slices = [slice(0, x) for x in shape]
offset = 0
for i in range(num_split):
    slices[split_dim] = slice(offset, offset + size_splits[i])
    offset += size_splits[i]
    self.assertAllEqual(result[i], inp[tuple(slices)])
