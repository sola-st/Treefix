# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_d9m_test.py
"""Modify testing of gradient for single-class case.

    The deterministic implementation does not produce the gradients expected by
    the original test (for the nondeterministic functionality) when the labels
    vector is not a valid probability distribution.

    labels: [[-1.], [0.], [1.], [1.]]
    logits: [[1.], [-1.], [0.], [1.]]

                   nondeterministic               deterministic
    dloss/dlogits: [[2.0], [1.0], [0.0], [0.0]]   [[0.0], [0.0], [0.0], [0.0]]

    Note that only the second two label vectors are valid probability
    distributions (as required by the API) and that the gradient matches for
    those cases.

    TODO(duncanriach): Further investigate the source of the difference in
                       the gradients for this case.
    """
self._testSingleClass(expected_gradient=[[0.0], [0.0], [0.0], [0.0]])
