# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ignore_errors_test.py
components = np.array([1., 2., 3., np.nan, 5.]).astype(np.float32)

dataset = (
    dataset_ops.Dataset.from_tensor_slices(components).map(
        lambda x: array_ops.check_numerics(x, "message")).ignore_errors())
get_next = self.getNext(dataset)

for x in [1., 2., 3., 5.]:
    self.assertEqual(x, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
