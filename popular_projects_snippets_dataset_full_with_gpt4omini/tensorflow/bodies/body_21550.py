# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# Build a while loop with `outer_body_fn`, export it, and verify that it can
# be imported and the gradient can be built and run correctly.
# pylint: disable=g-long-lambda
exit(self._testGradientSerDes(
    lambda x: control_flow_ops.while_loop(
        lambda i, y: i < 5, outer_body_fn, [0, x])[1]))
