# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
in_shape = LayerShapeNCDHW(
    batch=2, channels=8, depth=5, height=12, width=15)
filter_shape = FilterShape3D(
    depth=3, height=3, width=3, in_channels=8, out_channels=1)
in_op = self._random_data_op(in_shape)
filter_op = self._random_data_op(filter_shape)
self._assert_reproducible(lambda: nn_ops.conv3d(
    in_op,
    filter_op,
    strides=[1, 1, 1, 1, 1],
    padding='VALID',
    data_format='NCDHW',
    dilations=[1, 1, 2, 2, 2]))
