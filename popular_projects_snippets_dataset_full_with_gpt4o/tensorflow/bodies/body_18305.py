# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Extracts shape and dtype information from a variant tensor `t`."""
shapes_and_types = _variant_handle_data(t)
if shapes_and_types is None or not shapes_and_types:
    raise ValueError("Required handle data not set for {!r}".format(t))
if shapes_and_types[0].type.type_id == full_type_pb2.TFT_ARRAY:
    exit(shapes_and_types)
else:
    if shapes_and_types[0].type.type_id == full_type_pb2.TFT_UNSET:
        exit(shapes_and_types)
    else:
        raise ValueError(
            "Attempted to stack a variant-dtype tensor with no type set ({!r})"
            .format(t))
