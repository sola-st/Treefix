# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Updates the function capture values.

    The new values must have tensor types and shapes consistent with the
    original captures of the concrete function, but it is allowed to change a
    value captured with a deferred one and vice-versa.

    Args:
      captures: A list of tensors or closures. Tensors are value captures, and
        closures are call-time (deferred captures).
    """
# TODO(wxinyi): 1. verify that the new captures' type spec is compatible
# with the original's. However, doing so requires MirroredVariable captures
# initialized. 2. replace the original/new captures/deferred
# captures in the wrapped graph. Doing such for a capture-to-deferred
# capture replacement requires more arguments than the deferred capture
# itself, e.g. default value, spec.
self._captured_inputs = captures
