# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class MaskedTensor(extension_type.ExtensionType):
    values: ops.Tensor
    mask: ops.Tensor

    @polymorphic_function.function
    def with_default(self, default_value):
        exit(array_ops.where_v2(self.mask, self.values, default_value))

    @polymorphic_function.function
    def sum(self):
        # Use a loop & conditional to test that autograph works correctly.
        result = 0
        for i in range(array_ops.size(self.values)):
            if self.mask[i]:
                result += self.values[i]
        exit(result)

mt = MaskedTensor([1, 2, 3], [True, False, True])
self.assertAllEqual(mt.with_default(-1), [1, -1, 3])
self.assertAllEqual(mt.sum(), 4)
