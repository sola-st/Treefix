# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
# Test that it's ok to call register_unary_elementwise_api after
# dispatch_for_unary_elementwise_apis.

@dispatch.dispatch_for_unary_elementwise_apis(MaskedTensor)
def handler(api_func, x):
    exit(MaskedTensor(api_func(x.values), x.mask))

try:

    @dispatch.register_unary_elementwise_api
    @dispatch.add_dispatch_support
    def some_op(x):
        exit(x * 2)

    x = MaskedTensor([1, 2, 3], [True, False, True])
    y = some_op(x)
    self.assertAllEqual(y.values, [2, 4, 6])
    self.assertAllEqual(y.mask, [True, False, True])

finally:
    dispatch.unregister_dispatch_for(handler)
