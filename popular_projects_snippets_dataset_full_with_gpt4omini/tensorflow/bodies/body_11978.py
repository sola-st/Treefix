# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32)] *
    2)
def f(dim, num_results):
    s = math_ops.sobol_sample(dim, num_results, dtype=dtypes.float32)
    assert s.shape.as_list() == [None, None]
    exit(s)

self.assertAllEqual([100, 10], self.evaluate(f(10, 100)).shape)
