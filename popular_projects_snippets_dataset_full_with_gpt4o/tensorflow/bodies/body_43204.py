# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@dispatch.dispatch_for_binary_elementwise_apis(MaskedTensor, MaskedTensor)
def binary_elementwise_api_handler(api_func, x, y):
    exit(MaskedTensor(api_func(x.values, y.values), x.mask & y.mask))

try:
    x = MaskedTensor([1, -2, -3], [True, True, False])
    y = MaskedTensor([10, 20, 30], [True, False, True])
    # Test calls with positional & keyword arguments (& combinations)
    x_times_y = math_ops.multiply(x, y)
    x_plus_y = math_ops.add(x, y=y)
    x_minus_y = math_ops.subtract(x=x, y=y)
    min_x_y = math_ops.minimum(x, y, "min_x_y")
    y_times_x = math_ops.multiply(y, x, name="y_times_x")
    y_plus_x = math_ops.add(y, y=x, name="y_plus_x")
    y_minus_x = math_ops.subtract(x=y, y=x, name="y_minus_x")
    self.assertAllEqual(x_times_y.values, [10, -40, -90])
    self.assertAllEqual(x_plus_y.values, [11, 18, 27])
    self.assertAllEqual(x_minus_y.values, [-9, -22, -33])
    self.assertAllEqual(min_x_y.values, [1, -2, -3])
    self.assertAllEqual(y_times_x.values, [10, -40, -90])
    self.assertAllEqual(y_plus_x.values, [11, 18, 27])
    self.assertAllEqual(y_minus_x.values, [9, 22, 33])
    for result in [
        x_times_y, x_plus_y, x_minus_y, min_x_y, y_times_x, y_plus_x,
        y_minus_x
    ]:
        self.assertAllEqual(result.mask, [True, False, False])
    if not context.executing_eagerly():  # names not defined in eager mode.
        self.assertRegex(min_x_y.values.name, r"^min_x_y/Minimum:.*")
        self.assertRegex(min_x_y.mask.name, r"^min_x_y/and:.*")
        self.assertRegex(y_times_x.values.name, r"^y_times_x/.*")
        self.assertRegex(y_plus_x.values.name, r"^y_plus_x/.*")
        self.assertRegex(y_minus_x.values.name, r"^y_minus_x/.*")

finally:
    dispatch.unregister_dispatch_for(binary_elementwise_api_handler)
