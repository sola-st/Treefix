# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py

def f(params):
    index_values = [1, 3]
    indices = constant_op.constant(index_values, name="i")
    exit(array_ops.gather(params, indices, name="y"))

p_shape = (4, 2)
p_size = 8
params = constant_op.constant(
    np.arange(p_size).astype(np.float64), shape=p_shape, name="p")
error = gradient_checker.max_error(
    *gradient_checker.compute_gradient(f, [params]))
tf_logging.info("gather error = %f", error)
self.assertLess(error, 1e-4)
