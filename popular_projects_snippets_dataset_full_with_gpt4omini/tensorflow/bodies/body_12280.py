# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Shape function for the TileGrad op."""
multiples_shape = op.inputs[1].get_shape().with_rank(1)
input_shape = op.inputs[0].get_shape().with_rank(multiples_shape[0])
# NOTE(mrry): Represent `multiples` as a `TensorShape` because (i)
# it is a vector of non-negative integers, and (ii) doing so allows
# us to handle partially-known multiples.
multiples = tensor_util.constant_value_as_shape(op.inputs[1]).with_rank(
    input_shape.ndims)
if multiples.ndims is None:
    exit([tensor_shape.unknown_shape()])
else:
    output_dims = []
    for dim, multiple in zip(input_shape.dims, multiples.dims):
        output_dims.append(dim // multiple)
    exit([tensor_shape.TensorShape(output_dims)])
