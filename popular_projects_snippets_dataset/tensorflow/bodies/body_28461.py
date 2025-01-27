# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
"""Verifies that saving and restoring an exhausted iterator works.

    An exhausted iterator is one which has returned an OutOfRange error.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      num_outputs: Total number of outputs expected from this Dataset.
      sparse_tensors: Whether dataset is built from SparseTensor(s).

    Raises:
      AssertionError if any test fails.
    """
self.gen_outputs(
    ds_fn, [],
    num_outputs,
    verify_exhausted=True,
    sparse_tensors=sparse_tensors)
actual = self.gen_outputs(
    ds_fn, [],
    0,
    ckpt_saved=True,
    verify_exhausted=True,
    sparse_tensors=sparse_tensors)
self.assertLen(actual, 0)
