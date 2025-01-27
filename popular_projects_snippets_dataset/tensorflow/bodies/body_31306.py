# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        gen_nn_ops.softmax_cross_entropy_with_logits([0., 1., 2., 3.],
                                                     [0., 1., 0., 1.])
