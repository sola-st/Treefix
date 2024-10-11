# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
xs = MaskedTensorV3([[1], [2], [3]], [[True], [False], [True]])
x0 = MaskedTensorV3(xs.values[0], xs.mask[0])

ds = dataset_ops.DatasetV2.from_tensors(xs)
self.assertEqual(next(iter(ds)), xs)
ds = ds.unbatch()
self.assertEqual(next(iter(ds)), x0)

ds = dataset_ops.DatasetV2.from_tensor_slices(xs)
self.assertEqual(next(iter(ds)), x0)
ds = ds.batch(3, drop_remainder=True)
self.assertEqual(next(iter(ds)), xs)
