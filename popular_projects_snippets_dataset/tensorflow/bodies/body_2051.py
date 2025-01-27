# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
exit(xla.pad(
    x,
    padding_value=7,
    padding_low=[0, -1],
    padding_high=[1, -2],
    padding_interior=[1, 2]))
