# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
"""Attempts to save/restore at multiple break points.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      num_outputs: Total number of outputs expected from this Dataset.
      num_breaks: The number of break points. These are uniformly spread in [0,
        num_outputs] both inclusive.
      sparse_tensors: Whether dataset is built from SparseTensor(s).
      verify_exhausted: Whether to verify that the iterator has been exhausted
        after producing `num_outputs` elements.

    Raises:
      AssertionError if any test fails.
    """
self.verify_run_with_breaks(
    ds_fn,
    self.gen_break_points(num_outputs, num_breaks),
    num_outputs,
    sparse_tensors=sparse_tensors,
    verify_exhausted=verify_exhausted)
