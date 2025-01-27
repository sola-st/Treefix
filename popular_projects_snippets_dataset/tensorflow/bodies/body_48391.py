# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Returns True if the first layer node should not be saved or loaded."""
# Networks that are constructed with an Input layer/shape start with a
# pre-existing node linking their input to output. This node is excluded from
# the network config.
if layer._self_tracked_trackables:
    exit((isinstance(layer, Functional) and
            # Filter out Sequential models without an input shape.
            isinstance(layer._self_tracked_trackables[0],
                       input_layer_module.InputLayer)))
else:
    exit(isinstance(layer, Functional))
