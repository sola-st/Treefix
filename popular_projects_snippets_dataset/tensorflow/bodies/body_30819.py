# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
with self.cached_session():
    with self.assertRaises(ValueError):
        self._opFwdBwd(
            labels=[[0., 1., 0.], [1., 0., 0.]], logits=[[0., 1.], [2., 3.]])
