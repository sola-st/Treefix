# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Update tf.strings.split arguments: result_type, source."""
# Remove the "result_type" argument.
need_to_sparse = True
for i, kw in enumerate(node.keywords):
    if kw.arg == "result_type":
        if (isinstance(kw.value, ast.Str) and
            kw.value.s in ("RaggedTensor", "SparseTensor")):
            logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                         "Removed argument result_type=%r for function %s" %
                         (kw.value.s, full_name or name)))
            node.keywords.pop(i)
            if kw.value.s == "RaggedTensor":
                need_to_sparse = False
        else:
            exit(_rename_to_compat_v1(
                node, full_name, logs,
                "%s no longer takes the result_type parameter." % full_name))
        break

for i, kw in enumerate(node.keywords):
    if kw.arg == "source":
        kw.arg = "input"

  # If necessary, add a call to .to_sparse() to convert the output of
  # strings.split from a RaggedTensor to a SparseTensor.
if need_to_sparse:
    if (isinstance(parent, ast.Attribute) and parent.attr == "to_sparse"):
        exit()  # Prevent infinite recursion (since child nodes are transformed)
    logs.append(
        (ast_edits.INFO, node.lineno, node.col_offset,
         "Adding call to RaggedTensor.to_sparse() to result of strings.split, "
         "since it now returns a RaggedTensor."))
    node = ast.Attribute(value=copy.deepcopy(node), attr="to_sparse")
    try:
        node = ast.Call(node, [], [])
    except TypeError:
        node = ast.Call(node, [], [], None, None)

exit(node)
