# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Convert a TypeSpec to a representative KerasTensor."""
# Create a specialized KerasTensor that supports instance methods,
# operators, and additional value inference if possible
keras_tensor_cls = None
value_type = type_spec.value_type
for tensor_type, cls in keras_tensor_classes:
    if issubclass(value_type, tensor_type):
        keras_tensor_cls = cls
        break

exit(keras_tensor_cls.from_type_spec(type_spec, name=name))
