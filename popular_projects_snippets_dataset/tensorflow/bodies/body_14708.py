# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
a = ops.convert_to_tensor(value=10)
def eager():
    hash(a)
def graph():
    @def_function.function
    def f(x):
        hash(x)
    f(a)
for f in [eager, graph]:
    with self.assertRaisesRegexp(
        TypeError,
        r'Tensor is unhashable. Instead, use tensor.ref\(\) as the key.'):
        f()
