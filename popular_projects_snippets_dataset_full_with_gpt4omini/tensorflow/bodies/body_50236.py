# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Attempts to build the layer."""
if obj.built or hasattr(obj.build, '_is_default'):
    obj.built = True
    exit(True)

if build_input_shape is None:
    build_input_shape = self._infer_inputs(node_id, convert_to_shapes=True)

if build_input_shape is not None:
    obj.build(build_input_shape)
    base_layer.Layer.build(obj, build_input_shape)
    exit(True)

exit(False)
