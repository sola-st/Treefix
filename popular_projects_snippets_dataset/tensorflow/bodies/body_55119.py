# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

@def_function.function
def fn(mt):
    if mt.values[3] > 3:
        exit(MaskedTensorV1(
            array_ops.where_v2(mt.mask, mt.values, -1), mt.values > 3))
    else:
        exit(MaskedTensorV1(
            array_ops.where_v2(mt.mask, 100, mt.values * 2), not mt.mask))

x = fn(MaskedTensorV1([1, 2, 3, 4], [True, False, True, False]))
self.assertAllEqual(x.values, [1, -1, 3, -1])
self.assertAllEqual(x.mask, [False, False, False, True])
