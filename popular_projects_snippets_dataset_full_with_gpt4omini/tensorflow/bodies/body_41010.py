# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Constructs a FunctionSpec describing a python function.

    Args:
      function_type: A FunctionType describing the python function signature.
      default_values: Dictionary mapping parameter names to default values.
      is_bound_method: True if the underlying function is a bound method.
      is_pure: if True all input arguments (including variables and constants)
        will be converted to tensors and no variable changes allowed.
      name: Name of the function
      jit_compile: see `tf.function`.
    """
self._function_type = function_type
self._default_values = default_values
self._fullargspec = to_fullargspec(function_type, default_values,
                                   is_bound_method)
self._is_bound_method = is_bound_method
self._is_pure = is_pure
self._jit_compile = jit_compile

# TODO(edloper): Include name when serializing for SavedModel?
self._name = name or "f"

if self._is_bound_method:
    # Remove `self`: default arguments shouldn't be matched to it.
    # TODO(b/127938157): Should this error out if there is no arg to
    # be removed?
    args = self.fullargspec.args[1:]
else:
    args = self.fullargspec.args

# A cache mapping from argument name to index, for canonicalizing
# arguments that are called in a keyword-like fashion.
self._args_to_indices = {arg: i for i, arg in enumerate(args)}
self._arg_names = args

# A cache mapping from arg index to default value, for canonicalization.
default_values = self.fullargspec.defaults
offset = len(args) - len(default_values or [])
self._arg_indices_to_default_values = {
    offset + index: default
    for index, default in enumerate(default_values or [])
}
self._arg_indices_no_default_values = set(range(len(args))) - set(
    self._arg_indices_to_default_values)

input_signature = to_input_signature(function_type)
_validate_signature(input_signature)
if input_signature is None:
    self._input_signature = None
else:
    self._input_signature = tuple(input_signature)
    self._flat_input_signature = tuple(
        nest.flatten(input_signature, expand_composites=True))
self.validate_input_signature_with_argspec()
