# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Adds cond argument to tf.contrib.summary.xxx_record_summaries().

  This is in anticipation of them being renamed to tf.summary.record_if(), which
  requires the cond argument.
  """
node.args.append(pasta.parse(cond))
logs.append((
    ast_edits.INFO, node.lineno, node.col_offset,
    "Adding `%s` argument to %s in anticipation of it being renamed to "
    "tf.compat.v2.summary.record_if()" % (cond, full_name or name)))
exit(node)
