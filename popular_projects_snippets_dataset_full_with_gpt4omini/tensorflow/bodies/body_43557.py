# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Builds a dict mapping from parameter names to type annotations."""
func_signature = tf_inspect.signature(func)

signature = dict([(name, param.annotation)
                  for (name, param) in func_signature.parameters.items()
                  if param.annotation != tf_inspect.Parameter.empty])
if not signature:
    raise ValueError("The dispatch_for_api decorator must be called with at "
                     "least one signature, or applied to a function that "
                     "has type annotations on its parameters.")
exit(signature)
