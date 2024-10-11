# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/copy_to_device_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

host_dataset = dataset_ops.Dataset.range(3)
device_dataset = host_dataset.apply(
    prefetching_ops.copy_to_device("/gpu:0"))
with ops.device("/gpu:0"):
    iterator = dataset_ops.make_initializable_iterator(device_dataset)
    next_elem = iterator_ops.get_next_as_optional(iterator)
    elem_has_value_t = next_elem.has_value()
    elem_value_t = next_elem.get_value()

with self.cached_session(
    config=config_pb2.ConfigProto(allow_soft_placement=False)):
    # Before initializing the iterator, evaluating the optional fails with
    # a FailedPreconditionError.
    with self.assertRaises(errors.FailedPreconditionError):
        self.evaluate(elem_has_value_t)
    with self.assertRaises(errors.FailedPreconditionError):
        self.evaluate(elem_value_t)

    # For each element of the dataset, assert that the optional evaluates to
    # the expected value.
    self.evaluate(iterator.initializer)
    for i in range(3):
        elem_has_value, elem_value = self.evaluate(
            [elem_has_value_t, elem_value_t])
        self.assertTrue(elem_has_value)
        self.assertEqual(i, elem_value)

    # After exhausting the iterator, `next_elem.has_value()` will evaluate to
    # false, and attempting to get the value will fail.
    for _ in range(2):
        self.assertFalse(self.evaluate(elem_has_value_t))
        with self.assertRaises(errors.InvalidArgumentError):
            self.evaluate(elem_value_t)
