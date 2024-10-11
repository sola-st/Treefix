# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
x = MaskedTensorV2(
    values=[[1, 2, 3], [4, 5, 6]],
    mask=[[True, True, True], [True, False, True]])

@def_function.function
def add_to_x(y):
    exit(MaskedTensorV2(x.values + y.values, x.mask & y.mask))

actual = add_to_x(MaskedTensorV2([10, 20, 30], [False, True, True]))
expected = MaskedTensorV2(
    values=[[11, 22, 33], [14, 25, 36]],
    mask=[[False, True, True], [False, False, True]])
self.assertIsInstance(actual, MaskedTensorV2)
self.assertAllEqual(expected.values, actual.values)
self.assertAllEqual(expected.mask, actual.mask)
