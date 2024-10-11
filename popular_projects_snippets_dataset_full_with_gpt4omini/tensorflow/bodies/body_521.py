# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Transforms image.resize_* to image.resize(..., method=*, ...)."""
resize_method = name[7:].upper()
new_arg = ast.keyword(arg="method",
                      value=ast.Attribute(
                          value=ast.Attribute(
                              value=ast.Attribute(
                                  value=ast.Name(id="tf", ctx=ast.Load()),
                                  attr="image", ctx=ast.Load()),
                              attr="ResizeMethod", ctx=ast.Load()),
                          attr=resize_method, ctx=ast.Load()))

# Ensures a valid transformation when a positional name arg is given
if len(node.args) == 4:
    pos_arg = ast.keyword(arg="preserve_aspect_ratio",
                          value=node.args[-1])
    node.args = node.args[:-1]
    node.keywords.append(pos_arg)
if len(node.args) == 3:
    pos_arg = ast.keyword(arg="align_corners",
                          value=node.args[-1])
    node.args = node.args[:-1]

new_keywords = []
for kw in node.keywords:
    if kw.arg != "align_corners":
        new_keywords.append(kw)
node.keywords = new_keywords

# Python3 ast requires the args for the Attribute, but codegen will mess up
# the arg order if we just set them to 0.
new_arg.value.lineno = node.lineno
new_arg.value.col_offset = node.col_offset+100

node.keywords.append(new_arg)
if isinstance(node.func, ast.Attribute):
    node.func.attr = "resize"
else:
    assert isinstance(node.func, ast.Name)
    node.func.id = "resize"

logs.append((ast_edits.INFO, node.lineno, node.col_offset,
             "Changed %s call to tf.image.resize(..., "
             "method=tf.image.ResizeMethod.%s)." % (full_name,
                                                    resize_method)))
exit(node)
