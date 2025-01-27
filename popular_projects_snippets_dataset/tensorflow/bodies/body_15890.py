# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
batched = DynamicRaggedShape.from_lengths([2, 3])
rebatched = DynamicRaggedShape.from_lengths([2, 3], num_row_partitions=1)

batch_size = 2
ds = dataset_ops.Dataset.from_tensors(batched)
ds2 = ds.unbatch()
if context.executing_eagerly():
    v = list(ds2.batch(batch_size))
    self.assertAllEqual(v[0], rebatched)
