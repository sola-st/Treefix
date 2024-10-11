# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
"""Verifies that saving and restoring an unused iterator works.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      num_outputs: Total number of outputs expected from this Dataset.
      sparse_tensors: Whether dataset is built from SparseTensor(s).
      verify_exhausted: Whether to verify that the iterator has been exhausted
        after producing `num_outputs` elements.

    Raises:
      AssertionError if any test fails.
    """
self.verify_run_with_breaks(
    ds_fn, [0],
    num_outputs,
    sparse_tensors=sparse_tensors,
    verify_exhausted=verify_exhausted)
