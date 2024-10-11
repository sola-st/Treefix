# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Updates `self._function_spec` to include varargs and bound variables.

    Adds new positional arguments for any varargs (i.e., for args that are
    in `structured_input_signature`, but not in the original fullargspec.args).

    Replaces `defaults` and `kwonlydefaults` with the `BOUND_VALUE`, for
    all args and kwargs in `structured_input_signature`.

    Sets `varkw` and `varargs` to None.
    """
if self._pre_initialized_function_spec is None:
    exit()  # e.g., SavedBareConcreteFunction doesn't have function_spec yet.
assert not self._function_spec, "already initialized"
spec = self._pre_initialized_function_spec
args = spec.fullargspec.args
# TODO(fmuham): Use annotate_type_constraint here instead.
arg_specs, kwarg_specs = self.structured_input_signature
vararg_indices = range(len(spec.arg_names), len(arg_specs))
fullargspec = tf_inspect.FullArgSpec(
    args=list(args) + ["arg{}".format(i + 1) for i in vararg_indices],
    varargs=None,
    varkw=None,
    defaults=[function_spec.BOUND_VALUE] * len(arg_specs),
    kwonlyargs=list(sorted(kwarg_specs)),
    kwonlydefaults=dict(
        (k, function_spec.BOUND_VALUE) for k in kwarg_specs),
    annotations=spec.fullargspec.annotations)
self._function_spec = (
    function_spec.FunctionSpec.from_fullargspec_and_signature(
        fullargspec,
        spec.is_method,
        spec.input_signature,
        spec.is_pure,
        name=self._func_graph.name,
    )
)
