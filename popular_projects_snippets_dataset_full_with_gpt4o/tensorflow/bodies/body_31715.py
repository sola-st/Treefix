# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_d9m_test.py
"""Modify testing of gradient for labels-broadcast case.

    The deterministic implementation does not produce the gradients expected by
    the original test (for the nondeterministic functionality) when the labels
    vector (after broadcasting) is not a valid probability distribution.

    labels: [[0.], [2.], [0.25]]
    logits: [[1., 1., 1., 1.],
             [1., 2., 3., 4.],
             [1., 2., 3., 4.]]

    dloss/dlogits (nondeterministic):
        [[ 0.25 ,  0.25 ,  0.25 ,  0.25 ],
         [-1.968, -1.913, -1.763, -1.355],
         [-0.218, -0.163, -0.013,  0.394]]

    dloss/dlogits (determinsitic):
        [[ 0.   ,  0.   ,  0.   ,  0.   ],
         [-1.743, -1.303, -0.105,  3.150],
         [-0.218, -0.163, -0.013,  0.394]]

    Note that neither of the first two broadcast label vectors is a valid
    probability distribution (as required by the API) and that these are the
    cases that yield different gradients for nondeterministic vs determinsitic
    implementations.

    TODO(duncanriach): Further investigate the source of the difference in
                       the gradient for this case.
    """
self._testLabelsBroadcast(uniform_labels_gradient=[[
    0., 0., 0., 0.
], [-1.743, -1.303, -0.105, 3.150], [-0.218, -0.163, -0.013, 0.394]])
