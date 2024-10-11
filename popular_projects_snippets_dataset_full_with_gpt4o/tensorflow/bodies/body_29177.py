# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
if not gpu_compatible and test.is_gpu_available():
    self.skipTest("Test case not yet supported on GPU.")
ds = dataset_ops.Dataset.from_tensors(np_value).repeat(3)

if context.executing_eagerly():
    iterator = dataset_ops.make_one_shot_iterator(ds)
    # For each element of the dataset, assert that the optional evaluates to
    # the expected value.
    for _ in range(3):
        next_elem = iterator_ops.get_next_as_optional(iterator)
        self.assertIsInstance(next_elem, optional_ops.Optional)
        self.assertTrue(
            structure.are_compatible(
                next_elem.element_spec,
                structure.type_spec_from_value(tf_value_fn())))
        self.assertTrue(next_elem.has_value())
        self.assertValuesEqual(np_value, next_elem.get_value())
    # After exhausting the iterator, `next_elem.has_value()` will evaluate to
    # false, and attempting to get the value will fail.
    for _ in range(2):
        next_elem = iterator_ops.get_next_as_optional(iterator)
        self.assertFalse(self.evaluate(next_elem.has_value()))
        with self.assertRaises(errors.InvalidArgumentError):
            self.evaluate(next_elem.get_value())
else:
    iterator = dataset_ops.make_initializable_iterator(ds)
    next_elem = iterator_ops.get_next_as_optional(iterator)
    self.assertIsInstance(next_elem, optional_ops.Optional)
    self.assertTrue(
        structure.are_compatible(
            next_elem.element_spec,
            structure.type_spec_from_value(tf_value_fn())))
    # Before initializing the iterator, evaluating the optional fails with
    # a FailedPreconditionError. This is only relevant in graph mode.
    elem_has_value_t = next_elem.has_value()
    elem_value_t = next_elem.get_value()
    with self.assertRaises(errors.FailedPreconditionError):
        self.evaluate(elem_has_value_t)
    with self.assertRaises(errors.FailedPreconditionError):
        self.evaluate(elem_value_t)
    # Now we initialize the iterator.
    self.evaluate(iterator.initializer)
    # For each element of the dataset, assert that the optional evaluates to
    # the expected value.
    for _ in range(3):
        elem_has_value, elem_value = self.evaluate(
            [elem_has_value_t, elem_value_t])
        self.assertTrue(elem_has_value)
        self.assertValuesEqual(np_value, elem_value)

    # After exhausting the iterator, `next_elem.has_value()` will evaluate to
    # false, and attempting to get the value will fail.
    for _ in range(2):
        self.assertFalse(self.evaluate(elem_has_value_t))
        with self.assertRaises(errors.InvalidArgumentError):
            self.evaluate(elem_value_t)
