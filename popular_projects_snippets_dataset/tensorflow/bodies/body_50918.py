# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Fixes a FunctionDef proto to be loaded in current context.

  In particular, when loading a function library into an eager context, one
  must rename the functions to avoid conflicts with existent functions.

  Args:
    fdef: FunctionDef proto to fix. It is mutated in-place.
    functions: map from function name to a ConcreteFunction instance.
    shared_name_suffix: A unique string for this load which helps to avoid
      `shared_name` collisions across loads. Two functions from the same load
      using the same `shared_name` still need to share, but functions from
      different loads with the same `shared_name` should not.
    new_gradient_op_types: map from old gradient op type to newly generated op
      type.

  Returns:
    orig_name: original value of fdef.signature.name
  """
orig_name = fdef.signature.name
contains_unsaved_custom_gradients = False

for node_def in fdef.node_def:
    fix_node_def(node_def, functions, shared_name_suffix)
    op_type = _get_gradient_op_type(node_def)
    if op_type is not None:
        if op_type in new_gradient_op_types:
            node_def.attr["_gradient_op_type"].s = compat.as_bytes(
                new_gradient_op_types[op_type])
        else:
            contains_unsaved_custom_gradients = True
if contains_unsaved_custom_gradients:
    logging.warning(
        "Importing a function (%s) with ops with unsaved custom gradients. Will"
        " likely fail if a gradient is requested.", fdef.signature.name)

fdef.signature.name = _clean_function_name(fdef.signature.name)
exit(orig_name)
