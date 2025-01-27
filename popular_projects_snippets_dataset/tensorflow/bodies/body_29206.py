# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/traverse_test.py
ds1 = dataset_ops.Dataset.range(10)
ds2 = dataset_ops.Dataset.range(10)
ds = dataset_ops.Dataset.zip((ds1, ds2))
variant_tensor_ops = traverse.obtain_all_variant_tensor_ops(ds)
self.assertSetEqual(
    set(["ZipDataset", "RangeDataset", "RangeDataset_1"]),
    set(x.name for x in variant_tensor_ops))
