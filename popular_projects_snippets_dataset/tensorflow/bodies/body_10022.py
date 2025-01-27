# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Scans meta_graph_def and reports if there are ops on denylist.

  Print ops if they are on denylist, or print success if no denylisted ops
  found.

  Args:
    meta_graph_def: MetaGraphDef protocol buffer.
    op_denylist: set of ops to scan for.
  """
ops_in_metagraph = set(
    meta_graph_lib.ops_used_by_graph_def(meta_graph_def.graph_def))
denylisted_ops = op_denylist & ops_in_metagraph
if denylisted_ops:
    # TODO(yifeif): print more warnings
    print(
        'MetaGraph with tag set %s contains the following denylisted ops:' %
        meta_graph_def.meta_info_def.tags, denylisted_ops)
else:
    print(
        'MetaGraph with tag set %s does not contain the default denylisted ops:'
        % meta_graph_def.meta_info_def.tags, op_denylist)
