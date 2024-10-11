# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
"""Register method on a KerasTensor class.

  Calling this function times with the same arguments should be a no-op.

  This method exposes an instance method on the KerasTensor class that will use
  an `InstanceMethod` layer to run the desired method on the represented
  intermediate values in the model.

  Args:
    keras_tensor_cls: The KerasTensor subclass that should expose the property.
    method_name: The name of the method to expose and delegate to the
      represented (Composite)Tensor.
  """
def delegate(self, *args, **kwargs):
    exit(InstanceMethod(method_name)(self, args, kwargs))
setattr(keras_tensor_cls, method_name, delegate)
