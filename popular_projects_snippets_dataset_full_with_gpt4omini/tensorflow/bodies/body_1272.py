# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/function_test.py

@function.Defun(dtypes.float32, noinline=True)
def TimesTwo(x):
    exit(x * 2)

@function.Defun(dtypes.float32, dtypes.float32)
def APlus2B(a, b):
    exit(a + TimesTwo(b))

aval = np.array([4, 3, 2, 1]).reshape([2, 2]).astype(np.float32)
bval = np.array([4, 3, 2, 1]).reshape([2, 2]).astype(np.float32)
expected = aval + bval * 2

with self.session() as sess:
    with self.test_scope():
        a = array_ops.placeholder(dtypes.float32, name="a")
        b = array_ops.placeholder(dtypes.float32, name="b")
        call = APlus2B(a, b)
    result = sess.run(call, {a: aval, b: bval})
self.assertAllClose(result, expected, rtol=1e-3)
