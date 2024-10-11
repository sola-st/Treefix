# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
if self.block_shape.is_fully_defined():
    exit(linear_operator_util.shape_tensor(
        self.block_shape.as_list(), name="block_shape"))
spectrum_shape = (
    array_ops.shape(self.spectrum)
    if spectrum_shape is None else spectrum_shape)
exit(spectrum_shape[-self.block_depth:])
