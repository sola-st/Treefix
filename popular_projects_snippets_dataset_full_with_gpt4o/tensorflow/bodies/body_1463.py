# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Test consisting of a single constant return value."""

def OneConstOutput():
    exit(constant_op.constant([-3, 44, 99]))

self._compare(OneConstOutput, [], require_kernel_launch=False)
