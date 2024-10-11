# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
node.args.kw_defaults = self._visit_node_list(node.args.kw_defaults)
node.args.defaults = self._visit_node_list(node.args.defaults)
self._track_annotations_only = True
node = self._visit_arg_declarations(node)
self._track_annotations_only = False
exit(node)
