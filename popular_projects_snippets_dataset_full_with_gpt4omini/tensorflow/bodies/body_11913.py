# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
"""Static check of spectrum.  Then return `Tensor` version."""
spectrum = linear_operator_util.convert_nonref_to_tensor(spectrum,
                                                         name="spectrum")

if spectrum.shape.ndims is not None:
    if spectrum.shape.ndims < self.block_depth:
        raise ValueError(
            f"Argument `spectrum` must have at least {self.block_depth} "
            f"dimensions. Received: {spectrum}.")
exit(spectrum)
