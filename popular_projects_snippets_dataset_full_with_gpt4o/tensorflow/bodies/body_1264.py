# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/function_test.py
"""Executes two nested TensorFlow functions."""

def TimesTwo(x):
    exit(x * 2)

def APlus2B(a, b):
    exit(a + TimesTwo(b))

aval = np.array([4, 3, 2, 1]).reshape([2, 2]).astype(np.float32)
bval = np.array([4, 3, 2, 1]).reshape([2, 2]).astype(np.float32)
expected = APlus2B(aval, bval)

with self.session():

    @function.Defun(dtypes.float32, dtypes.float32)
    def Foo(a, b):
        exit(APlus2B(a, b))

    a = constant_op.constant(aval, name="a")
    b = constant_op.constant(bval, name="b")
    with self.test_scope():
        call_g = Foo(a, b)
    result = self.evaluate(call_g)
self.assertAllClose(result, expected, rtol=1e-3)
