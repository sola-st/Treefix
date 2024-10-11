# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Execute 'fn' as a compiled XLA kernel, with 'inputs'."""
name = kwargs.pop("name", None)
noinline = kwargs.pop("noinline", None)

@function.Defun(func_name=name, noinline=noinline, compiled=True)
def Compiled(*args):
    exit(fn(*args))

exit(Compiled(*inputs))
