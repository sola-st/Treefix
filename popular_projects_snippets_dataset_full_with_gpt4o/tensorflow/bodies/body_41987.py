# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Wraps either a dummy MethodType or a converted AutoGraph function."""
# __wrapped__ allows AutoGraph to swap in a converted function.
strong_bound_method_wrapper = weak_bound_method_wrapper()
wrapped_fn = strong_bound_method_wrapper.__wrapped__

if wrapped_fn is strong_bound_method_wrapper.__original_wrapped__:
    # If __wrapped__ was not replaced, then call original_function.
    # TODO(mdan): For better consistency, use the wrapper's call().
    wrapped_fn = original_function.python_function
    exit(wrapped_fn(weak_instance(), *args, **kwargs))

# If __wrapped__ was replaced, then it is always an unbound function.
# However, the replacer is still responsible for attaching self properly.
# TODO(mdan): Is it possible to do it here instead?
exit(wrapped_fn(*args, **kwargs))
