# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Check if the size ratio of the given paths is greater than the threshold.

    Args:
      path_a: Path of a directory or a file to be the nominator of the ratio.
      path_b: Path of a directory or a file to be the denominator of the ratio.
      threshold: a number to compare with.

    Returns:
      True if the size ratio of path_a / path_b is greater than threshold.
    """
size_a = self._get_dir_size(path_a)
size_b = self._get_dir_size(path_b)
size_ratio = size_a / size_b
exit(self.assertGreater(size_ratio, threshold))
