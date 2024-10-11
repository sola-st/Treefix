# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py

def f(params):
    index_values = [1, 3, 5, 6]
    indices = constant_op.constant(index_values, name="i")
    y = array_ops.gather(params, indices, name="y")
    index_values2 = [0, 2]
    indices2 = constant_op.constant(index_values2, name="i2")
    exit(array_ops.gather(y, indices2, name="y2"))

p_shape = (8, 2)
p_size = 16
params = constant_op.constant(
    np.arange(p_size).astype(np.float64), shape=p_shape, name="p")
error = gradient_checker.max_error(
    *gradient_checker.compute_gradient(f, [params]))
tf_logging.info("nested gather error = %f", error)
self.assertLess(error, 1e-4)
