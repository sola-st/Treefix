# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/traverse_test.py
ds = dataset_ops.Dataset.range(10)
variant_tensor_ops = traverse.obtain_all_variant_tensor_ops(ds)
self.assertAllEqual(["RangeDataset"], [x.name for x in variant_tensor_ops])
