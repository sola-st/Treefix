# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Register overloads for all operators."""
for operator in ops.Tensor.OVERLOADABLE_OPERATORS:
    cls._overload_operator(tensor_class, operator)

# We include `experimental_ref` for versions of TensorFlow that
# still include the deprecated method in Tensors.
if hasattr(tensor_class, 'experimental_ref'):
    cls._overload_operator(tensor_class, 'experimental_ref')
