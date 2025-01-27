# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Overload an operator with the same implementation as a base Tensor class.

    We pull the operator out of the class dynamically to avoid ordering issues.

    Args:
      tensor_class: The (Composite)Tensor to get the method from.
      operator: string. The operator name.
    """
tensor_oper = getattr(tensor_class, operator)

# Compatibility with Python 2:
# Python 2 unbound methods have type checks for the first arg,
# so we need to extract the underlying function
tensor_oper = getattr(tensor_oper, '__func__', tensor_oper)

setattr(cls, operator, tensor_oper)
