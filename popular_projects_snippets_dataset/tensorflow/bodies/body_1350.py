# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with ops.device('device:CPU:0'):
    y = 2.0 * x
exit((x, y))
