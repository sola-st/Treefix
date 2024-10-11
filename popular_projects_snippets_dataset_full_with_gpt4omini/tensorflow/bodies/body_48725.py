# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
# Preserve compatibility with older configs
flat_input_tensors = nest.flatten(input_tensors)
# If this is a single element but not a dict, unwrap. If this is a dict,
# assume the first layer expects a dict (as is the case with a
# DenseFeatures layer); pass through.
if not isinstance(input_tensors, dict) and len(flat_input_tensors) == 1:
    input_tensors = flat_input_tensors[0]
exit(input_tensors)
