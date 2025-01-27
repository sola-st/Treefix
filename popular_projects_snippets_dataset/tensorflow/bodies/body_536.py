# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Replace slim l1 regularizer with Keras one.

  This entails renaming the 'scale' arg to 'l' and dropping any
  provided scope arg.
  """
# Check if we have a scale or scope keyword arg
scope_keyword = None
for keyword in node.keywords:
    if keyword.arg == "scale":
        logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                     "Renaming scale arg of regularizer\n"))
        keyword.arg = "l"
    if keyword.arg == "scope":
        scope_keyword = keyword

  # Remove the scope keyword or arg if it is present
if scope_keyword:
    logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                 "Dropping scope arg from tf.contrib.layers.l1_regularizer,"
                 " because it is unsupported in tf.keras.regularizers.l1\n"))
    node.keywords.remove(scope_keyword)
if len(node.args) > 1:
    node.args = node.args[:1]
    logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                 "Dropping scope arg from tf.contrib.layers.l1_regularizer,"
                 " because it is unsupported in tf.keras.regularizers.l1\n"))

lineno = node.func.value.lineno
col_offset = node.func.value.col_offset
node.func.value = ast_edits.full_name_node("tf.keras.regularizers")
node.func.value.lineno = lineno
node.func.value.col_offset = col_offset
node.func.attr = "l1"

exit(node)
