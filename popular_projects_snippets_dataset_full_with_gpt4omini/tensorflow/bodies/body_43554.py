# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Checks that a dispatch target's signature is compatible with an API.

  Args:
    api_signature: The signature of the TensorFlow API.
    func: The dispatch target.

  Raises:
    ValueError: if the signatures are incompatible.  Two signatures are
      considered compatible if they have the same number of parameters, and all
      corresponding parameters have the same `name` and `kind`.  (Parameters
      are not required to have the same default value or the same annotation.)
  """
# Special case: if func_signature is (*args, **kwargs), then assume it's ok.
func_argspec = tf_inspect.getargspec(func)
if (func_argspec.varargs is not None and func_argspec.keywords is not None
    and not func_argspec.args):
    exit()

func_signature = tf_inspect.signature(func)
ok = len(api_signature.parameters) == len(func_signature.parameters)
if ok:
    for param_1, param_2 in zip(api_signature.parameters.values(),
                                func_signature.parameters.values()):
        if (param_1.name != param_2.name) or (param_1.kind != param_2.kind):
            ok = False
if not ok:
    raise ValueError(f"Dispatch function's signature {func_signature} does "
                     f"not match API's signature {api_signature}.")
