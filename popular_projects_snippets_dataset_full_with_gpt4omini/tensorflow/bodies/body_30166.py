# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
value = np.array(value).astype(self.tensor_type.as_numpy_dtype)
# Give the value a non-zero imaginary component for complex types.
if self.tensor_type.is_complex:
    value -= 1j * value

with test_util.device(use_gpu=True):
    if self._use_resource:
        var = resource_variable_ops.ResourceVariable(self.x)
    else:
        var = variables.Variable(self.x)
    self.test.evaluate(var.initializer)
    val = self.test.evaluate(var[index].assign(value))
    # val_copy is used to check that tf.compat.v1.assign works equivalently
    # to the assign method above.
    val_copy = self.test.evaluate(state_ops.assign(var[index], value))
    valnp = np.copy(self.x_np)
    valnp[index] = np.array(value)
    self.test.assertAllEqual(val, valnp)
    self.test.assertAllEqual(val_copy, valnp)
