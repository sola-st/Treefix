# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
c = np.random.randint(0, 2, 6).astype(np.bool_).reshape(1, 3, 2)  # pylint: disable=too-many-function-args
x = np.random.rand(1, 3, 2) * 100
y = np.random.rand(1, 3, 2) * 100
for t in [np.float16, np.float32, np.float64]:
    with self.subTest(t=t):
        xt = x.astype(t)
        yt = y.astype(t)
        if t == np.float16:
            # Compare fp16 theoretical gradients to fp32 numerical gradients,
            # since fp16 numerical gradients are too imprecise unless great
            # care is taken with choosing the inputs and the delta. This is
            # a weaker check (in particular, it does not test the op itself,
            # only its gradient), but it's much better than nothing.
            self._compareGradientX(fn, c, xt, yt, np.float64)
            self._compareGradientY(fn, c, xt, yt, np.float64)
        else:
            self._compareGradientX(fn, c, xt, yt)
            self._compareGradientY(fn, c, xt, yt)
