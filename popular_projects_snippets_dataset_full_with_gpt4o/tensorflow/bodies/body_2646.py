# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
padding_config = xla_client.PaddingConfig()
for lo, hi, interior in [(1, 2, 1), (0, 1, 0)]:
    dimension = xla_client.PaddingConfigDimension()
    dimension.edge_padding_low = lo
    dimension.edge_padding_high = hi
    dimension.interior_padding = interior
    padding_config.dimensions.append(dimension)
ops.Pad(
    ops.Constant(c, NumpyArrayF32([[1.0, 2.0], [3.0, 4.0]])),
    ops.Constant(c, NumpyArrayF32(0.0)), padding_config)
self._ExecuteAndCompareClose(
    c,
    expected=[[[0.0, 0.0, 0.0], [1.0, 2.0, 0.0], [0.0, 0.0, 0.0],
               [3.0, 4.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]])
