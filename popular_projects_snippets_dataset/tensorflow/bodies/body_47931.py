# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
"""Register property on a KerasTensor class.

  Calling this multiple times with the same arguments should be a no-op.

  This method exposes a property on the KerasTensor class that will use an
  `InstanceProperty` layer to access the property on the represented
  intermediate values in the model.

  Args:
    keras_tensor_cls: The KerasTensor subclass that should expose the property.
    property_name: The name of the property to expose and delegate to the
      represented (Composite)Tensor.
  """
# We use a lambda because we can't create a Keras layer at import time
# due to dynamic layer class versioning.
property_access = property(lambda self: InstanceProperty(property_name)(self))  # pylint: disable=unnecessary-lambda
setattr(keras_tensor_cls, property_name, property_access)
