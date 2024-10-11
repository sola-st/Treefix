# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Asserts that a dataset produces the expected output / error.

    Args:
      dataset: A dataset to check for the expected output / error.
      expected_output: A list of elements that the dataset is expected to
        produce.
      expected_shapes: A list of TensorShapes which is expected to match
        output_shapes of dataset.
      expected_error: A tuple `(type, predicate)` identifying the expected error
        `dataset` should raise. The `type` should match the expected exception
        type, while `predicate` should either be 1) a unary function that inputs
        the raised exception and returns a boolean indicator of success or 2) a
        regular expression that is expected to match the error message
        partially.
      requires_initialization: Indicates that when the test is executed in graph
        mode, it should use an initializable iterator to iterate through the
        dataset (e.g. when it contains stateful nodes). Defaults to False.
      num_test_iterations: Number of times `dataset` will be iterated. Defaults
        to 1.
      assert_items_equal: Tests expected_output has (only) the same elements
        regardless of order.
      expected_error_iter: How many times to iterate before expecting an error,
        if an error is expected.
    """
self.assertTrue(
    expected_error is not None or expected_output is not None,
    "Exactly one of expected_output or expected error should be provided.")
if expected_error:
    self.assertTrue(
        expected_output is None,
        "Exactly one of expected_output or expected error should be provided."
    )
    with self.assertRaisesWithPredicateMatch(expected_error[0],
                                             expected_error[1]):
        get_next = self.getNext(
            dataset, requires_initialization=requires_initialization)
        for _ in range(expected_error_iter):
            self.evaluate(get_next())
    exit()
if expected_shapes:
    self.assertEqual(expected_shapes,
                     dataset_ops.get_legacy_output_shapes(dataset))
self.assertGreater(num_test_iterations, 0)
for _ in range(num_test_iterations):
    get_next = self.getNext(
        dataset, requires_initialization=requires_initialization)
    result = []
    for _ in range(len(expected_output)):
        try:
            result.append(self.evaluate(get_next()))
        except errors.OutOfRangeError:
            raise AssertionError(
                "Dataset ended early, producing %d elements out of %d. "
                "Dataset output: %s" %
                (len(result), len(expected_output), str(result)))
    self._compareOutputToExpected(result, expected_output, assert_items_equal)
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(get_next())
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(get_next())
