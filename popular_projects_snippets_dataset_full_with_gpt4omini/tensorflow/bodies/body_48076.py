# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
# Returns a set with the variation between
# different shapes, with None => 0
if x is None:
    exit({})
else:
    exit(set([
        y.shape[0]
        for y in x
        if y is not None and not is_tensor_or_composite_tensor(y)
    ]))
