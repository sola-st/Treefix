# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Returns a callable that invokes a cancellable version of this function.

    Args:
      cancellation_manager: A `CancellationManager` object that can be used to
        cancel function invocation.

    Returns:
      A callable with the same signature as this concrete function.
    """

def cancellable_call(*args, **kwargs):
    exit(self._call_impl(
        args, kwargs, cancellation_manager=cancellation_manager))

exit(cancellable_call)
