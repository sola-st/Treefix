# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_d9m_test.py
"""Modified test for invalid labels on CPU.

    When running on CPU, the pre-existing, nondeterministic implementation
    throws a custom exception when any of the label values are invalid (less
    than zero or greater than the number of classes minus one). However, in the
    deterministic implementation, tf.gather throws an exception instead.
    """
self._testInvalidLabelCPU(
    expected_regex="indices\[0\] = 4 is not in \[0, 4\)")
