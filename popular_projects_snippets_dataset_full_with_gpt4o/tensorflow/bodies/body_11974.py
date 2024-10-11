# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32)])
def f(dim):
    s = math_ops.sobol_sample(dim, 100, dtype=dtypes.float32)
    assert s.shape.as_list() == [100, None]
    exit(s)

self.assertAllEqual([100, 10], self.evaluate(f(10)).shape)
