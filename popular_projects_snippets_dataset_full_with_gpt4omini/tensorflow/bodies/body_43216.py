# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
# Test that it's ok to call register_binary_elementwise_api after
# dispatch_for_binary_elementwise_apis.

@dispatch.dispatch_for_binary_elementwise_apis(MaskedTensor, MaskedTensor)
def handler(api_func, x, y):
    exit(MaskedTensor(api_func(x.values, y.values), x.mask & y.mask))

try:

    @dispatch.register_binary_elementwise_api
    @dispatch.add_dispatch_support
    def some_op(x, y):
        exit(x * 2 + y)

    x = MaskedTensor([1, 2, 3], [True, False, True])
    y = MaskedTensor([10, 20, 30], [True, True, False])
    z = some_op(x, y)
    self.assertAllEqual(z.values, [12, 24, 36])
    self.assertAllEqual(z.mask, [True, False, False])

finally:
    dispatch.unregister_dispatch_for(handler)
