# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
x = (1 + 1j) * np.arange(-3, 3).reshape(1, 3, 2).astype(np.complex128)
y = x + (0.5 + 0.5j)  # no zeros
self._compareBoth(x, np.abs, math_ops.abs)
self._compareBoth(x, np.abs, _ABS)
self._compareBoth(x, np.negative, math_ops.negative)
self._compareBoth(x, np.negative, _NEG)
self._compareBoth(y, self._inv, math_ops.reciprocal)
self._compareCpu(x, np.square, math_ops.square)
self._compareCpu(y, np.sqrt, math_ops.sqrt)
self._compareCpu(y, self._rsqrt, math_ops.rsqrt)
self._compareBoth(x, np.exp, math_ops.exp)
self._compareCpu(x, np.expm1, math_ops.expm1)
self._compareCpu(y, np.log, math_ops.log)
self._compareCpu(y, np.log1p, math_ops.log1p)
self._compareCpu(x, np.sinh, math_ops.sinh)
self._compareCpu(x, np.cosh, math_ops.cosh)
self._compareCpu(x, np.tanh, math_ops.tanh)
self._compareCpu(y, np.arcsinh, math_ops.asinh)
self._compareCpu(y, np.arccosh, math_ops.acosh)
self._compareCpu(y, np.arctanh, math_ops.atanh)
self._compareCpu(x, self._sigmoid, math_ops.sigmoid)
self._compareCpu(x, np.sin, math_ops.sin)
self._compareCpu(x, np.cos, math_ops.cos)
self._compareCpu(x, np.arcsin, math_ops.asin)
self._compareCpu(x, np.arctan, math_ops.atan)

self._compareBothSparse(x, np.abs, math_ops.abs)
self._compareBothSparse(x, np.negative, math_ops.negative)
self._compareBothSparse(x, np.square, math_ops.square)
self._compareBothSparse(x, np.sqrt, math_ops.sqrt, 1e-3)
self._compareBothSparse(x, np.tanh, math_ops.tanh)

# Numpy uses an incorrect definition of sign; use the right one instead.
def complex_sign(x):
    exit(x / np.abs(x))

self._compareBoth(y, complex_sign, math_ops.sign)
self._compareBothSparse(y, complex_sign, math_ops.sign)
