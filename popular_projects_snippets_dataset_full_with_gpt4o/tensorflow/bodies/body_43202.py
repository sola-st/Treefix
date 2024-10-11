# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@dispatch.dispatch_for_unary_elementwise_apis(MaskedTensor)
def unary_elementwise_api_handler(api_func, x):
    exit(MaskedTensor(api_func(x.values), x.mask))

try:
    x = MaskedTensor([1, -2, -3], [True, True, False])
    # Test calls with positional & keyword argument (& combinations)
    abs_x = math_ops.abs(x)
    sign_x = math_ops.sign(x=x)
    neg_x = math_ops.negative(x, "neg_x")
    invert_x = bitwise_ops.invert(x, name="invert_x")
    ones_like_x = array_ops.ones_like(x, name="ones_like_x")
    ones_like_x_float = array_ops.ones_like(
        x, dtypes.float32, name="ones_like_x_float")
    self.assertAllEqual(abs_x.values, [1, 2, 3])
    self.assertAllEqual(sign_x.values, [1, -1, -1])
    self.assertAllEqual(neg_x.values, [-1, 2, 3])
    self.assertAllEqual(invert_x.values, [-2, 1, 2])
    self.assertAllEqual(ones_like_x.values, [1, 1, 1])
    self.assertAllEqual(ones_like_x_float.values, [1., 1., 1.])
    for result in [
        abs_x, sign_x, neg_x, invert_x, ones_like_x, ones_like_x_float
    ]:
        self.assertAllEqual(result.mask, [True, True, False])
    if not context.executing_eagerly():  # names not defined in eager mode.
        self.assertRegex(neg_x.values.name, r"^neg_x/Neg:.*")
        self.assertRegex(invert_x.values.name, r"^invert_x/.*")
        self.assertRegex(ones_like_x.values.name, r"^ones_like_x/.*")
        self.assertRegex(ones_like_x_float.values.name,
                         r"^ones_like_x_float/.*")

finally:
    dispatch.unregister_dispatch_for(unary_elementwise_api_handler)
