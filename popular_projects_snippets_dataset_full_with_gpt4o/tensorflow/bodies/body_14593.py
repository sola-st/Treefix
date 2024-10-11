# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
# Backing tensor is the same if copy=False, other attributes being None.
self.assertIs(np_array_ops.array(zeros_list, copy=False), zeros_list)
self.assertIs(np_array_ops.array(zeros_list, copy=False), zeros_list)

# Backing tensor is different if ndmin is not satisfied.
self.assertIsNot(
    np_array_ops.array(zeros_list, copy=False, ndmin=2),
    zeros_list)
self.assertIsNot(
    np_array_ops.array(zeros_list, copy=False, ndmin=2),
    zeros_list)
self.assertIs(
    np_array_ops.array(zeros_list, copy=False, ndmin=1),
    zeros_list)
self.assertIs(
    np_array_ops.array(zeros_list, copy=False, ndmin=1),
    zeros_list)

# Backing tensor is different if dtype is not satisfied.
self.assertIsNot(
    np_array_ops.array(zeros_list, copy=False, dtype=int),
    zeros_list)
self.assertIsNot(
    np_array_ops.array(zeros_list, copy=False, dtype=int),
    zeros_list)
self.assertIs(
    np_array_ops.array(zeros_list, copy=False, dtype=float),
    zeros_list)
self.assertIs(
    np_array_ops.array(zeros_list, copy=False, dtype=float),
    zeros_list)
