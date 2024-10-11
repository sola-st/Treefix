# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
idx = [
    [0, 1, 0, 1],
    [0, 0, 0, 1],
]
states = math_ops.log([
    [[1.0, 2.0, 3.0, 4.0],
     [5.0, 6.0, 7.0, 8.0]],
    [[0.1, 0.2, 0.3, 0.4],
     [0.5, 0.6, 0.7, 0.8]],
])
sum_of_states = math_ops.exp(ctc_ops._sum_states(idx, states))
self.assertAllClose([
    [[4.0, 6.0, 0.0, 0.0],
     [18.0, 8.0, 0.0, 0.0]],
    [[0.4, 0.6, 0.0, 0.0],
     [1.8, 0.8, 0.0, 0.0]]
], sum_of_states)
