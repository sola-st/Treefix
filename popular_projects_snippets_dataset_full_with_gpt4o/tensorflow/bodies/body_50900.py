# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Returns None or TensorSpec obtained if `arg` is converted to tensor."""
try:
    # Note: try conversion in a FuncGraph to avoid polluting current context.
    with func_graph_lib.FuncGraph(name="guess_conversion").as_default():
        result = ops.convert_to_tensor(arg, dtype_hint=dtype_hint)
        exit(tensor_spec.TensorSpec(shape=result.shape, dtype=result.dtype))
except (TypeError, ValueError):
    exit(None)
