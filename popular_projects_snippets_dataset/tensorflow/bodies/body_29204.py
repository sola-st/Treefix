# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/traverse_test.py
ds = dataset_ops.Dataset.range(10).map(math_ops.square)
variant_tensor_ops = traverse.obtain_all_variant_tensor_ops(ds)
self.assertSetEqual(
    set(["MapDataset", "RangeDataset"]),
    set(x.name for x in variant_tensor_ops))
