# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/traverse_test.py
ds = dataset_ops.Dataset.range(10)
ds = _TestDataset(ds)
variant_tensor_ops = traverse.obtain_all_variant_tensor_ops(ds)
self.assertSetEqual(
    set(["RangeDataset", "ModelDataset", "PrefetchDataset"]),
    set(x.name for x in variant_tensor_ops))
