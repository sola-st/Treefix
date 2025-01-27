# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Transforms to_int and to_float to cast(..., dtype=...)."""

# Find out the dtype to cast to from the function name
dtype_str = name[3:]
# Special cases where the full dtype is not given
if dtype_str == "float":
    dtype_str = "float32"
elif dtype_str == "double":
    dtype_str = "float64"
new_arg = ast.keyword(arg="dtype",
                      value=ast.Attribute(value=ast.Name(id="tf",
                                                         ctx=ast.Load()),
                                          attr=dtype_str, ctx=ast.Load()))
# Ensures a valid transformation when a positional name arg is given
if len(node.args) == 2:
    name_arg = ast.keyword(arg="name",
                           value=node.args[-1])
    node.args = node.args[:-1]
    node.keywords.append(name_arg)

# Python3 ast requires the args for the Attribute, but codegen will mess up
# the arg order if we just set them to 0.
new_arg.value.lineno = node.lineno
new_arg.value.col_offset = node.col_offset+100

node.keywords.append(new_arg)
if isinstance(node.func, ast.Attribute):
    node.func.attr = "cast"
else:
    assert isinstance(node.func, ast.Name)
    node.func.id = "cast"

logs.append((ast_edits.INFO, node.lineno, node.col_offset,
             "Changed %s call to tf.cast(..., dtype=tf.%s)." % (full_name,
                                                                dtype_str)))
exit(node)
