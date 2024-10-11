# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_d9m_test.py
"""Test exception-throwing for non-statically-shaped, zero-rank labels.

    The deterministic implementation cannot check for this case because it does
    not have a specific implementation of SparseSoftmaxXentWithLogitsOp.
    Instead tf.gather, which is used to create the deterministic implementation,
    throws an error.
    """
self._testScalarHandling(
    expected_regex="Expected batch_dims in the range \[0, 0\], but got 1.*")
