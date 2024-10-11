# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
default = ops.Tensor._USE_EQUALITY

try:
    def _v1_check(a, b):
        self.assertEqual(a, a)
        self.assertIs(a, a)
        self.assertNotEqual(a, 1.0)
        self.assertIsNot(a, 1.0)
        self.assertNotEqual(a, b)
        self.assertIsNot(a, b)

    def _v2_check(a, b):
        self.assertEqual(a, a)
        self.assertIs(a, a)
        self.assertEqual(a, 1.0)
        self.assertIsNot(a, 1.0)
        self.assertEqual(a, b)
        self.assertIsNot(a, b)

    constant_a = constant_op.constant(1.0)
    constant_b = constant_op.constant(1.0)

    ops.disable_tensor_equality()
    self._test_hashable(constant_a, constant_b, True)
    _v1_check(constant_a, constant_b)
    ops.enable_tensor_equality()
    _v2_check(constant_a, constant_b)
    self._test_hashable(constant_a, constant_b, False)

    variable_a = variables.Variable(1.0)
    variable_b = variables.Variable(1.0)

    ops.disable_tensor_equality()
    _v1_check(variable_a, variable_b)
    self._test_hashable(variable_a, variable_b, True)
    ops.enable_tensor_equality()
    _v2_check(variable_a, variable_b)
    self._test_hashable(variable_a, variable_b, False)

    # We only test numpy behaviour in v2 mode since we'd like to match that.
    numpy_a = np.array(1.0)
    numpy_b = np.array(1.0)
    _v2_check(numpy_a, numpy_b)
    self._test_hashable(numpy_a, numpy_b, False)
finally:
    if default:
        ops.enable_tensor_equality()
    else:
        ops.disable_tensor_equality()
