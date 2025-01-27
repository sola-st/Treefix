# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py

@function.Defun(dtypes.int32, dtypes.int32)
def test_func(a, b):
    exit(a + b)

x = constant_op.constant([1], name='x_const')
y = constant_op.constant([2], name='y_const')
test_func(x, y, name='func_call')  # pylint: disable=unexpected-keyword-arg
