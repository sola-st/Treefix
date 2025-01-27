# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
ragged = DynamicRaggedShape.from_lengths([4, 5, 2, 3])
ds = dataset_ops.DatasetV2.from_tensors(ragged)
dsu = ds.unbatch()
if context.executing_eagerly():
    values = list(dsu)
    self.assertAllEqual(values[0].static_lengths(), [5, 2, 3])
    self.assertAllEqual(values[2].static_lengths(), [5, 2, 3])

dsb = dsu.batch(2)
if context.executing_eagerly():
    valuesb = list(dsb)
    self.assertAllEqual(valuesb[0].static_lengths(), [2, 5, 2, 3])
    self.assertAllEqual(valuesb[1].static_lengths(), [2, 5, 2, 3])
