# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/layer_serialization.py

exit(dict(
    class_name=type(self.obj).__name__,
    name=self.obj.name,
    dtype=self.obj.dtype,
    sparse=self.obj.sparse,
    ragged=self.obj.ragged,
    batch_input_shape=self.obj._batch_input_shape,  # pylint: disable=protected-access
    config=self.obj.get_config()))
