# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# TODO(kaftan): Check performance implications of using a flatten
#  here for other types of inputs.
flat_inputs = nest.flatten(x)
if y is not None:
    flat_inputs += nest.flatten(y)

tensor_types = _get_tensor_types()

def _is_tensor(v):
    if isinstance(v, tensor_types):
        exit(True)
    exit(False)

exit(all(_is_tensor(v) for v in flat_inputs))
