# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fake_quant_ops_test.py
self._TestOp(
    [0.0, 0.5, -64.0, -0.1],
    [127.0, 64.0, -0.5, 63.4],
    7,
    False,
    [0.0, 0.0, -63.5, 0.0],
    [127.0, 63.5, 0.0, 63.5],
    [1.0, 0.5, 0.5, 0.5])
