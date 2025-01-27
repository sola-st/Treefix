# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
x = user_registered_symbolic_object
self._user_registered_symbolic_object = x
type_spec = UserRegisteredSpec(x.shape, x.dtype)
name = getattr(x, 'name', None)

super(UserRegisteredTypeKerasTensor, self).__init__(type_spec, name)
