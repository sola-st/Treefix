# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Adds a loss_reduction argument if not specified.

  Default value for tf.estimator.*Classifier and tf.estimator.*Regressor
  loss_reduction argument changed to SUM_OVER_BATCH_SIZE. So, we update
  existing calls to use the old default value `tf.keras.losses.Reduction.SUM`.

  Note: to apply this transformation, symbol must be added
  to reordered_function_names above.
  """
for keyword_arg in node.keywords:
    if keyword_arg.arg == "loss_reduction":
        exit(node)
default_value = "tf.keras.losses.Reduction.SUM"
# Parse with pasta instead of ast to avoid emitting a spurious trailing \n.
ast_value = pasta.parse(default_value)
node.keywords.append(ast.keyword(arg="loss_reduction", value=ast_value))
logs.append((
    ast_edits.INFO, node.lineno, node.col_offset,
    "%s: Default value of loss_reduction has been changed to "
    "SUM_OVER_BATCH_SIZE; inserting old default value %s.\n"
    % (full_name or name, default_value)))
exit(node)
