# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
# size_splits too big
with self.assertRaises(ValueError):
    array_ops.split([0, 1], [3, -1], axis=0)

# Correct inference of variable dimension
s0, s1 = array_ops.split([0, 1, 2], [2, -1], axis=0)
assert s0.shape.as_list() == [2]
assert s1.shape.as_list() == [1]
