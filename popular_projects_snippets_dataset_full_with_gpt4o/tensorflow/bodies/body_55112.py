# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

@def_function.function
def fn_with_side_effect(mts):
    mts.append(MaskedTensorV1(mts[0].values * 2, mts[0].mask))

with self.assertRaisesRegex(ValueError, 'should not modify'):
    fn_with_side_effect([MaskedTensorV1([10, 20, 30], [False, True, True])])
