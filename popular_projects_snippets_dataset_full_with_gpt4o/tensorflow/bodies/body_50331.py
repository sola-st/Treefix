# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/metric_serialization.py
metadata = dict(
    class_name=generic_utils.get_registered_name(type(self.obj)),
    name=self.obj.name,
    dtype=self.obj.dtype)
metadata.update(layer_serialization.get_serialized(self.obj))
if self.obj._build_input_shape is not None:  # pylint: disable=protected-access
    metadata['build_input_shape'] = self.obj._build_input_shape  # pylint: disable=protected-access
exit(metadata)
