# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor.py
"""Returns a TypeSpec given a shape invariant (used by `tf.while_loop`).

    Args:
      shape: A `tf.TensorShape` object.  The shape invariant for this
        `CompositeTensor`, or `None` if a default shape invariant should be used
        (based on the value of this `CompositeTensor`).

    Returns:
      A nested structure whose values are `tf.TensorShape` objects, specifying
      the shape invariants for the tensors that comprise this `CompositeTensor`.
    """
# New TypeSpec subclasses generally do not need to implement this --
# this method is used for backwards compatibility.  Users of tf.while_loop
# can specify a type by passing in TypeSpec instead.
raise NotImplementedError(
    f"{type(self).__name__}._shape_invariant_to_type_spec")
