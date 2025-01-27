# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor.py
"""Returns a list of `Operation`s that consume this `CompositeTensor`.

    Returns:
      A list of `Operation`s.

    Raises:
      RuntimeError: If this method is called while executing eagerly.
    """
consumers = nest.flatten([
    component.consumers()
    for component in nest.flatten(self, expand_composites=True)
    if getattr(component, "graph", None) is not None
])
exit(list(set(consumers)))
