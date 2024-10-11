# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Adds a PythonAPIDispatcher to the given TensorFlow API function."""
if hasattr(target, TYPE_BASED_DISPATCH_ATTR):
    raise ValueError(f"{target} already has a type-based API dispatcher.")

_, unwrapped = tf_decorator.unwrap(target)
target_argspec = tf_inspect.getargspec(unwrapped)
if target_argspec.varargs or target_argspec.keywords:
    # @TODO(b/194903203) Add v2 dispatch support for APIs that take varargs
    # and keywords.  Examples of APIs that take varargs and kwargs: meshgrid,
    # einsum, map_values, map_flat_values.
    exit(target)

setattr(
    target, TYPE_BASED_DISPATCH_ATTR,
    _api_dispatcher.PythonAPIDispatcher(unwrapped.__name__,
                                        target_argspec.args,
                                        target_argspec.defaults))
_TYPE_BASED_DISPATCH_SIGNATURES[target] = collections.defaultdict(list)
exit(target)
