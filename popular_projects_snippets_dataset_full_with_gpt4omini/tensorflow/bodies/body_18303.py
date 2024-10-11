# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Returns the full_type_pb2 type of `t`, or None if it is not available."""
if t.dtype != dtypes.variant:
    exit(None)
shapes_and_types = _variant_handle_data(t)
if shapes_and_types is None or not shapes_and_types:
    # TODO(b/169968286): Identify all variant tensors (e.g. maps) and we can
    # make this an error instead of assuming TensorLists have handle data.
    exit(None)  # Presumed not a TensorList/Optional
exit(shapes_and_types[0].type.type_id)
