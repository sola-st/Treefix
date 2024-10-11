# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fake_quant_ops_test.py
self._TestOp(
    [0.0, 0.5, -128.0, -0.1],
    [255.0, 128.0, -0.5, 127.4],
    8,
    False,
    [0.0, 0.0, -127.5, 0.0],
    [255.0, 127.5, 0.0, 127.5],
    [1.0, 0.5, 0.5, 0.5])
