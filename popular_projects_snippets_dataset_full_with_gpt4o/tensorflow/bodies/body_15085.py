# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
batched = ragged_factory_ops.constant([[0], [1], [2], [3]])
ds = dataset_ops.Dataset.from_tensors(batched)
ds2 = ds.unbatch()
ds3 = ds2.unbatch()
if context.executing_eagerly():
    value = next(iter(ds3))
    self.assertAllEqual(0, value)
