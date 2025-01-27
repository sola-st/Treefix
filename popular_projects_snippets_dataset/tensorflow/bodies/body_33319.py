# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
# Check that the op does not loop forever on infinite inputs. (b/158433036)
in_tensor = [[np.inf, 1.], [1., 1.]]
result = self.evaluate(linalg_impl.matrix_exponential(in_tensor))
self.assertTrue(np.all(np.isnan(result)))
