# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Test consisting of a constant zero element return value."""

def ConstZeroElementOutput():
    exit(array_ops.fill([7, 0], 3.0))

self._compare(ConstZeroElementOutput, [], require_kernel_launch=False)
