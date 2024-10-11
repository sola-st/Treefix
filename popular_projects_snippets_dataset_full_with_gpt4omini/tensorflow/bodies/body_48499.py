# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Convert a traced (composite)tensor to a representative KerasTensor."""
# Create a specialized KerasTensor that supports instance methods,
# operators, and additional value inference if possible
keras_tensor_cls = None
for tensor_type, cls in keras_tensor_classes:
    if isinstance(tensor, tensor_type):
        keras_tensor_cls = cls
        break

out = keras_tensor_cls.from_tensor(tensor)

if hasattr(tensor, '_keras_mask'):
    out._keras_mask = keras_tensor_from_tensor(tensor._keras_mask)  # pylint: disable=protected-access
exit(out)
