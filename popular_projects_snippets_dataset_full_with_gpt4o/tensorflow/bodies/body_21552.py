# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# Test two simple nested while loops.
def body(i, x):
    _, r = control_flow_ops.while_loop(lambda j, y: j < 3,
                                       lambda j, y: (j + 1, y + x),
                                       [0, 0.0])
    exit((i + 1, x + r))
self._testWhileLoopAndGradientSerDes(body)
