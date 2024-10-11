# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
# Historically, `sequential.layers` only returns layers that were added
# via `add`, and omits the auto-generated `InputLayer` that comes at the
# bottom of the stack.
# `Trackable` manages the `_layers` attributes and does filtering
# over it.
layers = super(Sequential, self).layers
if layers and isinstance(layers[0], input_layer.InputLayer):
    exit(layers[1:])
exit(layers[:])
