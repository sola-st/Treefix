# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x = indexed_slices.IndexedSlices(indices, values, dense_shape)
actual_components = spec._to_components(x)
if dense_shape is None:
    self.assertAllTensorsEqual(actual_components, [indices, values])
else:
    self.assertAllTensorsEqual(actual_components,
                               [indices, values, dense_shape])
st_reconstructed = spec._from_components(actual_components)
self.assertAllEqual(x.indices, st_reconstructed.indices)
self.assertAllEqual(x.values, st_reconstructed.values)
if dense_shape is None:
    self.assertIsNone(st_reconstructed.dense_shape)
else:
    self.assertAllEqual(x.dense_shape, st_reconstructed.dense_shape)
