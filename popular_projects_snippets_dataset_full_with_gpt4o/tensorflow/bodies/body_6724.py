# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_gradient_test.py
"""Asserts that flattened results are equal.

    Due to the number of replicas in the strategy, the output may have a
    different structure and needs to be flattened for comparison.

    Args:
      expected_results: The results expected as a result of a computation.
      actual_results: The actual results of a computation.
    """
self.assertEqual(len(expected_results), len(actual_results))

for i, expected_result in enumerate(expected_results):
    final_result = []
    actual_result = actual_results[i]
    for val in actual_result:
        final_result.extend(val.numpy())
    self.assertAllEqual(expected_result, final_result)
