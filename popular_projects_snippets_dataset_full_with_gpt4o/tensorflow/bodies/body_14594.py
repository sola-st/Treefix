# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
ndmins = [0, 1, 2, 5]
for a, dtype, ndmin, copy in itertools.product(self.all_arrays,
                                               self.all_types, ndmins,
                                               [True, False]):
    self.match(
        np_array_ops.array(a, dtype=dtype, ndmin=ndmin, copy=copy),
        np.array(a, dtype=dtype, ndmin=ndmin, copy=copy))

zeros_list = np_array_ops.zeros(5)

def test_copy_equal_false():
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

test_copy_equal_false()
with ops.device('CPU:1'):
    test_copy_equal_false()

self.assertNotIn('CPU:1', zeros_list.backing_device)
with ops.device('CPU:1'):
    self.assertIn(
        'CPU:1', np_array_ops.array(zeros_list, copy=True).backing_device)
    self.assertIn(
        'CPU:1', np_array_ops.array(np.array(0), copy=True).backing_device)
