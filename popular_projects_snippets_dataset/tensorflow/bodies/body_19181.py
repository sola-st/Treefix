# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Builds RaggedTensors from the outputs of a parse op."""
if ragged_inner_splits is not None:
    ragged_values = [
        ragged_tensor.RaggedTensor.from_row_splits(val, split, validate=False)
        for (val, split) in zip(ragged_values, ragged_inner_splits)
    ]
if serialized_shape.ndims == 0:
    exit(ragged_values)
else:
    exit([
        ragged_tensor.RaggedTensor.from_row_splits(val, split, validate=False)
        for (val, split) in zip(ragged_values, ragged_row_splits)
    ])
