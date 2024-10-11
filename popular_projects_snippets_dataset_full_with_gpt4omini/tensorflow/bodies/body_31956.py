# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
"""Verifies the output shape of the Conv3D op when output tensor is empty.

    Args: none
    """
input_shape = [0, 112, 112, 112, 32]
filter_shape = [3, 3, 3, 32, 64]

output_shape = [0, 112, 112, 112, 64]
input_data = 1
filter_data = 1
for data_type in self._DtypesToTest(False):
    input_tensor = constant_op.constant(
        input_data, shape=input_shape, dtype=data_type, name="input")
    filter_tensor = constant_op.constant(
        filter_data, shape=filter_shape, dtype=data_type, name="filter")
    conv = nn_ops.conv3d(
        input_tensor,
        filter_tensor,
        strides=[1, 1, 1, 1, 1],
        dilations=[1, 1, 1, 1, 1],
        padding="SAME",
        data_format="NDHWC",
        name="conv")
    values = self.evaluate(conv)
    self.assertEqual(values.shape, tensor_shape.TensorShape(output_shape))
