# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
# Note: The "tensor_equals" API has no "name" argument.
signature = {"self": MaskedTensor, "other": MaskedTensor}

@dispatch.dispatch_for_api(math_ops.tensor_equals, signature)
def masked_tensor_equals(self, other):
    del self, other

dispatch.unregister_dispatch_for(masked_tensor_equals)  # clean up.

with self.assertRaisesRegexp(
    ValueError, r"Dispatch function's signature \(self, other, name=None\) "
    r"does not match API's signature \(self, other\)\."):

    @dispatch.dispatch_for_api(math_ops.tensor_equals, signature)
    def masked_tensor_equals_2(self, other, name=None):
        del self, other, name

    del masked_tensor_equals_2  # avoid pylint unused variable warning.
