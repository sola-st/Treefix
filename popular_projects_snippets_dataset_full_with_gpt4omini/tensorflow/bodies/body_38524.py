# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py

def compute_f32(np_func):
    """Decorator to compute Numpy function with float32 math."""

    def f(x):
        y = np_func(x.astype(np.float32))
        exit(y.astype(x.dtype))

    exit(f)

bfloat16 = dtypes_lib.bfloat16.as_numpy_dtype
x = np.arange(-6, 6,
              2).reshape(1, 3, 2).astype(bfloat16)
w = x - x.min() + 1.1  # all greater than 1
y = (x + .5).astype(bfloat16)  # no zero
z = (x + 15.5).astype(bfloat16)  # all positive
k = np.arange(-0.90, 0.90, 0.05).astype(bfloat16)  # between -1 and 1
self._compareBoth(x, np.abs, math_ops.abs)
self._compareBoth(x, np.abs, _ABS)
self._compareBoth(x, np.negative, math_ops.negative)
self._compareBoth(x, np.negative, _NEG)
self._compareBoth(y, compute_f32(self._inv), math_ops.reciprocal)
self._compareCpu(x, np.exp, math_ops.exp)
self._compareCpu(x, np.expm1, math_ops.expm1)
self._compareCpu(z, compute_f32(np.log), math_ops.log)
self._compareCpu(z, compute_f32(np.log1p), math_ops.log1p)
self._compareBoth(y, np.sign, math_ops.sign)
self._compareCpu(z, self._rsqrt, math_ops.rsqrt)
self._compareBoth(x, compute_f32(np.sin), math_ops.sin)
self._compareBoth(x, compute_f32(np.cos), math_ops.cos)
self._compareBoth(x, compute_f32(np.tan), math_ops.tan)
self._compareBoth(x, compute_f32(np.sinh), math_ops.sinh)
self._compareBoth(x, compute_f32(np.cosh), math_ops.cosh)
self._compareBoth(x, compute_f32(np.tanh), math_ops.tanh)
self._compareBoth(k, compute_f32(np.arcsin), math_ops.asin)
self._compareBoth(k, compute_f32(np.arccos), math_ops.acos)
self._compareBoth(x, compute_f32(np.arctan), math_ops.atan)
self._compareBoth(x, compute_f32(np.arcsinh), math_ops.asinh)
self._compareBoth(w, compute_f32(np.arccosh), math_ops.acosh)
self._compareBoth(k, compute_f32(np.arctanh), math_ops.atanh,
                  grad_tol=1e-2)
self._compareBoth(x, compute_f32(np.vectorize(math.erf)), math_ops.erf)
self._compareBoth(x, compute_f32(np.vectorize(math.erfc)), math_ops.erfc)
self._compareBoth(x, compute_f32(np.square), math_ops.square)
