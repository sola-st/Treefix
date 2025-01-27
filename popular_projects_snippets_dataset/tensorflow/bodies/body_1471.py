# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Tests an operator that has a mandatory-constant shape input."""

def FillWithFloat(x):
    exit(array_ops.fill(x, 9.5))

self._compare(FillWithFloat, [np.array([3, 2], dtype=np.int32)])
