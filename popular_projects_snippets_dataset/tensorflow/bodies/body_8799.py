# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
"""Makes an iterable from datasets created by the given function.

    Args:
      dataset_fn: A function that returns a `Dataset`.
      coordinator: a `ClusterCoordinator` object, used to create dataset
        resources.
    """

def disallow_variable_creation(next_creator, **kwargs):
    raise ValueError("Creating variables in `dataset_fn` is not allowed.")

if isinstance(dataset_fn, def_function.Function):
    with variable_scope.variable_creator_scope(disallow_variable_creation):
        dataset_fn = dataset_fn.get_concrete_function()
elif not isinstance(dataset_fn, tf_function.ConcreteFunction):
    with variable_scope.variable_creator_scope(disallow_variable_creation):
        dataset_fn = def_function.function(dataset_fn).get_concrete_function()
self._dataset_fn = dataset_fn
self._coordinator = coordinator
self._element_spec = None
