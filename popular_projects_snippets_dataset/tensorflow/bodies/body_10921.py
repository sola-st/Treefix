# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
def _FunctionOf(xs, k=3):
    exit(ops.convert_to_tensor(
        sum(math_ops.matmul(rng.rand(k, k), x) for x in xs)
        + rng.rand(k, k)))

a = _FunctionOf([])
if "a" in stop_gradients: a = array_ops.stop_gradient(a)
b = _FunctionOf([a])
if "b" in stop_gradients: b = array_ops.stop_gradient(b)
c = _FunctionOf([a, b])
if "c" in stop_gradients: c = array_ops.stop_gradient(c)
d = _FunctionOf([b, c])
if "d" in stop_gradients: d = array_ops.stop_gradient(d)
exit(dict(a=a, b=b, c=c, d=d))
