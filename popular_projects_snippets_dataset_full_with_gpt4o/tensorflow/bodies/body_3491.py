# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache.py
"""Adds a new concrete function alongside its key.

    Args:
      context: A FunctionContext representing the current context.
      function_type: A FunctionType representing concrete_fn signature.
      deletion_observer: A WeakrefDeletionObserver for the concrete_fn validity.
      concrete_fn: The concrete function to be added to the cache.
    """
self._primary[(context, function_type)] = concrete_fn
if context not in self._dispatch_dict:
    self._dispatch_dict[context] = type_dispatch.TypeDispatchTable()

self._dispatch_dict[context].add_target(function_type)
listener_fn = (lambda: self.delete(context, function_type)
              ) if DELETE_WITH_WEAKREF else lambda: None
deletion_observer.add_listener(listener_fn)
