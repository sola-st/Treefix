# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
ragged = DynamicRaggedShape.from_lengths([2, 3])
ds = dataset_ops.DatasetV2.from_tensors(ragged)
dsu = ds.unbatch()
if context.executing_eagerly():
    values = list(dsu)
    self.assertAllEqual(values[0].static_lengths(), [3])
    self.assertAllEqual(values[1].static_lengths(), [3])
