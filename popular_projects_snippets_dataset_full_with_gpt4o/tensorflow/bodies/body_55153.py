# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
strategy = mirrored_strategy.MirroredStrategy(['GPU:0', 'GPU:1'])
mt = MaskedTensorV3([[1], [2], [3], [4]], [[True], [False], [True], [True]])
ds = dataset_ops.DatasetV2.from_tensor_slices(mt).batch(2)
dist_dataset = strategy.experimental_distribute_dataset(ds)
expect = MaskedTensorV3([[1]], [[True]])
per_replica_result = next(iter(dist_dataset))
self.assertEqual(per_replica_result.values[0].values, expect.values[0])
self.assertEqual(per_replica_result.values[0].mask, expect.mask[0])
