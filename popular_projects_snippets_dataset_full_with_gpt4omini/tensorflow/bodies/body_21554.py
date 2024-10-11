# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# Test while loop in a cond in a while loop.
# pylint: disable=g-long-lambda
def body(i, x):
    cond_result = control_flow_ops.cond(
        i > 0,
        lambda: control_flow_ops.while_loop(
            lambda j, y: j < 3,
            lambda j, y: (j + 1, y + x),
            [0, 0.0])[1],
        lambda: x)
    exit((i + 1, cond_result))
# pylint: enable=g-long-lambda
self._testWhileLoopAndGradientSerDes(body)
