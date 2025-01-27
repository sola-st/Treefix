# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Regression test for compiled functions that return an aliased buffer.

       XLA returns aliased buffers if outputs are identical. Tests that
       we handle that case.
    """

def AddOnceReturnTwice(x):
    y = math_ops.add(x, x)
    exit((y, y))

# Exercises compiling a function (say, Foo) which calls another function
# (say, Bar) which is not inlined. When the compiler compiles Foo, it needs
# to symbolically execute Bar correctly regardless of whether Bar is inlined
# or not.

# Tests compiled=True and noinline=True.
self._compare(
    AddOnceReturnTwice, [np.array([[[0.5, -1.0]]], dtype=np.float32)],
    name="AddOnceReturnTwice_inline",
    noinline=True)

# Tests compiled=True and noinline=False.
self._compare(
    AddOnceReturnTwice, [np.array([[[0.5, -1.0]]], dtype=np.float32)],
    name="AddOnceReturnTwice_noinline",
    noinline=False)
