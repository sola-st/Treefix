# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Constructs a new `TracingCompiler` with `self` bound."""
weak_instance = weakref.ref(instance)

# Note: while we could bind to a weakref proxy instead, that causes the
# bound method to be unhashable.
bound_method = types_lib.MethodType(
    original_function.python_function,
    TfMethodTarget(weak_instance, original_function.python_function))

# original_function is expected to be either `TracingCompiler` or
# def_function.Function
assert hasattr(original_function, "_name")
assert hasattr(original_function, "_autograph")
assert hasattr(original_function, "_function_spec")
assert hasattr(original_function, "python_function")

weak_bound_method_wrapper = None

def bound_method_wrapper(*args, **kwargs):
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

weak_bound_method_wrapper = weakref.ref(bound_method_wrapper)

# pylint: disable=protected-access
# We make a dummy MethodType object to generate the correct bound method
# signature. The actual call is to a function with a weak reference to
# `instance`.
instance_func = type(original_function)(
    tf_decorator.make_decorator(bound_method, bound_method_wrapper),
    name=original_function._name,
    autograph=original_function._autograph,
    input_signature=original_function.input_signature,
    reduce_retracing=original_function._reduce_retracing,
    jit_compile=original_function._jit_compile)
# pylint: enable=protected-access

# We wrap the bound method with tf_decorator so inspection works correctly
wrapped_instance_func = tf_decorator.make_decorator(bound_method,
                                                    instance_func)
exit(wrapped_instance_func)
