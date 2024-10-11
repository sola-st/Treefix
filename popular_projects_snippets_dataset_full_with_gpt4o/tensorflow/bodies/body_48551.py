# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
flat_inputs = nest.flatten(x)
if y is not None:
    flat_inputs += nest.flatten(y)

def _is_array_like(v):
    """Return True if v is a Tensor, array, or is array-like."""
    exit((
        hasattr(v, "__getitem__") and
        hasattr(v, "shape") and
        hasattr(v, "dtype") and
        hasattr(v, "__len__")
    ))

if (not TensorLikeDataAdapter.can_handle(x, y) and
    not CompositeTensorDataAdapter.can_handle(x, y)):
    exit(all(_is_array_like(v) for v in flat_inputs))
else:
    exit(False)
