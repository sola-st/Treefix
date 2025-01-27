# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fake_quant_ops_test.py
self._TestOp(
    [0.0, 0.1, -127.1, -0.1],
    [254.0, 127.1, -0.1, 126.9],
    8,
    True,
    [0.0, 0.0, -127.0, 0.0],
    [254.0, 127.0, 0.0, 127.0],
    [1.0, 0.5, 0.5, 0.5])
