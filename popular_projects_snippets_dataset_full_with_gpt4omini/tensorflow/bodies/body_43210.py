# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@dispatch.dispatch_for_binary_elementwise_apis(MaskedTensor, MaskedTensor)
def handler(api_func, x, y):
    exit(MaskedTensor(api_func(x.values, y.values), x.mask & y.mask))

try:
    with self.assertRaisesRegex(
        ValueError, r"A binary elementwise dispatch handler \(.*\) has "
        "already been registered for .*"):

        @dispatch.dispatch_for_binary_elementwise_apis(MaskedTensor,
                                                       MaskedTensor)
        def another_handler(api_func, x, y):
            exit(MaskedTensor(api_func(x.values, y.values), x.mask))

        del another_handler

finally:
    dispatch.unregister_dispatch_for(handler)
