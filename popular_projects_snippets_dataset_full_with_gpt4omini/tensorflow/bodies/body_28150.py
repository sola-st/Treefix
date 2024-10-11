# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unique_test.py
"""Test the `unique()` transformation on a list of test cases.

    Args:
      dtype: The `dtype` of the elements in each test case.
      test_cases: A list of pairs of lists. The first component is the test
        input that will be passed to the transformation; the second component is
        the expected sequence of outputs from the transformation.
    """

# The `current_test_case` will be updated when we loop over `test_cases`
# below; declare it here so that the generator can capture it once.
current_test_case = []
dataset = dataset_ops.Dataset.from_generator(lambda: current_test_case,
                                             dtype).unique()

for test_case, expected in test_cases:
    current_test_case = test_case
    self.assertDatasetProduces(dataset, [
        compat.as_bytes(element) if dtype == dtypes.string else element
        for element in expected
    ])
