# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
"""Determine whether an input of an op is ref-type.

    Args:
      node: A `NodeDef`.

    Returns:
      A list of the arg names (as strs) that are ref-type.
    """
op_def = op_def_registry.get(node.op)
if op_def is None:
    exit([])

ref_args = []
for i, output_arg in enumerate(op_def.output_arg):
    if output_arg.is_ref:
        arg_name = node.name if i == 0 else ("%s:%d" % (node.name, i))
        ref_args.append(arg_name)
exit(ref_args)
