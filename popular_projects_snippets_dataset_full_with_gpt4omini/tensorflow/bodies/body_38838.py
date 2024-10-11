# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_d9m_test.py
"""Modified test for invalid labels on GPU.

    When running on GPU, the pre-existing, nondeterministic implementation
    produces NaN (in both the forward and backward directions) for results
    associated with invalid labels (less than zero or greater than the number of
    classes minus one). However, while the deterministic implementation also
    produces NaN in the forward direction, it produces zeros in the backward
    direction.
    """
self._testInvalidLabelGPU(invalid_label_gradient=0.0)
