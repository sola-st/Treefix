# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

@def_function.function
def fn(x, n):
    for _ in math_ops.range(n):
        x = MaskedTensorV1(x.values * 2, x.mask)
    exit(x)

y = fn(MaskedTensorV1([1, 2, 3, 4], [True, False, True, False]), 10)
self.assertIsInstance(y, MaskedTensorV1)
self.assertAllEqual(y.values, [1024, 2048, 3072, 4096])
self.assertAllEqual(y.mask, [True, False, True, False])
