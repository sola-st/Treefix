# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ignore_errors_test.py
components = np.array([1., 2., 3., np.nan, 5.]).astype(np.float32)
dataset = (
    dataset_ops.Dataset.from_tensor_slices(components).map(
        lambda x: array_ops.check_numerics(x, "message")).ignore_errors(
            log_warning=True))
get_next = self.getNext(dataset)
with self.captureWritesToStream(sys.stderr) as logged:
    for x in [1., 2., 3.]:
        self.assertEqual(x, self.evaluate(get_next()))
    self.assertEqual(5., self.evaluate(get_next()))
expected = "Tensor had NaN values"
self.assertIn((expected), logged.contents())
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
