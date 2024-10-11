# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Test an int32-typed input.

       On a GPU, int32 tensors will be placed in host memory.
    """

def AddToSelf(x):
    exit(math_ops.add(x, x))

self._compare(AddToSelf, [np.array([7, 1, 3], dtype=np.int32)])
