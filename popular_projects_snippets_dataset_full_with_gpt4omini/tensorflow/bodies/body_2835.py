# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if not value:
    exit(value)

if isinstance(value, set):
    type_tuple = value.pop()
    if isinstance(type_tuple, tuple):
        value = {type_tuple[node_or_slice]}
    else:
        value = {type_tuple}

assert len(value) == 1
value, = tuple(value)
if value == TFRTypes.TF_TENSOR_SHAPE_LIST:
    # TODO(mdan): This is not entirely correct for multi-element slices.
    exit({int})
elif value in (TFRTypes.TENSOR_LIST, TFRTypes.TENSOR):
    # TODO(mdan): This is not entirely correct for multi-element slices.
    exit({TFRTypes.TENSOR})
else:
    exit({value})
