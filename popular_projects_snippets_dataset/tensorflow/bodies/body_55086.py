# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
mt1 = MaskedTensorV2([1, 2, 3, 4], [True, True, False, True])
mt2 = extension_type.pack(mt1)

for mt in [mt1, mt2]:
    with self.assertRaisesRegex(
        AttributeError,
        'Cannot mutate attribute `score` outside the custom constructor of ExtensionType'
    ):
        mt.score = 12
    with self.assertRaisesRegex(
        AttributeError,
        'Cannot mutate attribute `values` outside the custom constructor of ExtensionType'
    ):
        mt.values = constant_op.constant([4, 3, 2, 1])
    with self.assertRaisesRegex(
        AttributeError,
        'Cannot mutate attribute `values` outside the custom constructor of ExtensionType'
    ):
        del mt.values
