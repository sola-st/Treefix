# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32)])
def f(num_results):
    s = math_ops.sobol_sample(10, num_results, dtype=dtypes.float32)
    assert s.shape.as_list() == [None, 10]
    exit(s)

self.assertAllEqual([100, 10], self.evaluate(f(100)).shape)
