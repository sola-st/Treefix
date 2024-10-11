# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
mt = MaskedTensorV3([[1], [2], [3]], [[True], [False], [True]])
ds = dataset_ops.DatasetV2.from_tensors(mt)
self.assertEqual(next(iter(ds)), mt)
