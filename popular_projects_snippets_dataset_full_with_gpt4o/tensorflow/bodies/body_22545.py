# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object.py
"""Creates a `SaveableObject` object.

    Args:
      op: the "producer" object that this class wraps; it produces a list of
        tensors to save.  E.g., a "Variable" object saving its backing tensor.
      specs: a list of SaveSpec, each element of which describes one tensor to
        save under this object. All Tensors must be on the same device.
      name: the name to save the object under.
    """
self.op = op
self.specs = specs
self.name = name
