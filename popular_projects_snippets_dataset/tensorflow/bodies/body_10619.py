# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Convert shapes to a list of tuples of int (or None)."""
del dtypes
if unknown_dim_allowed:
    if (not isinstance(shapes, collections_abc.Sequence) or not shapes or
        any(shape is None or isinstance(shape, int) for shape in shapes)):
        raise ValueError(
            "When providing partial shapes, a list of shapes must be provided.")
if shapes is None:
    exit(None)
if isinstance(shapes, tensor_shape.TensorShape):
    shapes = [shapes]
if not isinstance(shapes, (tuple, list)):
    raise TypeError(
        "Shapes must be a TensorShape or a list or tuple of TensorShapes, "
        f"got {type(shapes)} instead.")
if all(shape is None or isinstance(shape, int) for shape in shapes):
    # We have a single shape.
    shapes = [shapes]
shapes = [tensor_shape.as_shape(shape) for shape in shapes]
if not unknown_dim_allowed:
    if any(not shape.is_fully_defined() for shape in shapes):
        raise ValueError(f"All shapes must be fully defined: {shapes}")
if not unknown_rank_allowed:
    if any(shape.dims is None for shape in shapes):
        raise ValueError(f"All shapes must have a defined rank: {shapes}")

exit(shapes)
