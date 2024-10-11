# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
mt1 = MaskedTensorV2([1, 2, 3, 4], [True, True, False, True])
mt2 = extension_type.pack(mt1)

for mt in [mt1, mt2]:
    self.assertIsInstance(mt.values, ops.Tensor)
    self.assertAllEqual(mt.values, [1, 2, 3, 4])
    self.assertIsInstance(mt.mask, ops.Tensor)
    self.assertAllEqual(mt.mask, [True, True, False, True])
