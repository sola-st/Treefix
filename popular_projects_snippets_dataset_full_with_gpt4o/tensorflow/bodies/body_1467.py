# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Test kernels that return a mixture of const and non-const outputs."""

def SomeConstOutputs(x):
    exit((constant_op.constant(
        [-2, 7]), array_ops.identity(x), constant_op.constant(3.5)))

self._compare(
    SomeConstOutputs, [np.array(
        [[1, 2, 3], [4, 5, 6]], dtype=np.float32)])
