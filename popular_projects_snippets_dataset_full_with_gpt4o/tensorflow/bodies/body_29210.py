# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/traverse_test.py
ds1 = dataset_ops.Dataset.range(10).repeat(10)

def map_fn(ds):

    def _map(x):
        exit(ds.batch(x))

    exit(_map)

ds2 = dataset_ops.Dataset.range(20).prefetch(1)
ds2 = ds2.flat_map(map_fn(ds1))
variant_tensor_ops = traverse.obtain_all_variant_tensor_ops(ds2)
self.assertSetEqual(
    set([
        "FlatMapDataset", "PrefetchDataset", "RepeatDataset",
        "RangeDataset", "RangeDataset_1"
    ]), set(x.name for x in variant_tensor_ops))
