# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
self._shape = tensor_shape.TensorShape(shape)
self._build_input_shape = self._shape
# Create new state variables
self._total = self.add_weight(
    'total', shape=shape, initializer=init_ops.zeros_initializer)
self._count = self.add_weight(
    'count', shape=shape, initializer=init_ops.zeros_initializer)
with ops.init_scope():
    if not context.executing_eagerly():
        backend._initialize_variables(backend._get_session())  # pylint: disable=protected-access
self._built = True
