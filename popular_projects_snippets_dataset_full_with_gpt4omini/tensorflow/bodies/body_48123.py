# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/input_layer.py
if self._init_type_spec is not None:
    config = {
        'name': self.name,
        'type_spec': self._init_type_spec
    }
else:
    config = {
        'batch_input_shape': self._batch_input_shape,
        'dtype': self.dtype,
        'sparse': self.sparse,
        'ragged': self.ragged,
        'name': self.name,
    }
exit(config)
