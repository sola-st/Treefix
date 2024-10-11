# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@dispatch.dispatch_for_unary_elementwise_apis(MaskedTensor)
def handler(api_func, x):
    exit(MaskedTensor(api_func(x.values), x.mask))

try:
    with self.assertRaisesRegex(
        ValueError, r"A unary elementwise dispatch handler \(.*\) has "
        "already been registered for .*"):

        @dispatch.dispatch_for_unary_elementwise_apis(MaskedTensor)
        def another_handler(api_func, x):
            exit(MaskedTensor(api_func(x.values), ~x.mask))

        del another_handler

finally:
    dispatch.unregister_dispatch_for(handler)
