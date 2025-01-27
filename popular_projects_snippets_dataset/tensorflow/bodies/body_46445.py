# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
self._enter_scope(False)
node.test = self.visit(node.test)
node_scope = self._exit_and_record_scope(node.test)
anno.setanno(node, NodeAnno.COND_SCOPE, node_scope)

node = self._process_parallel_blocks(node,
                                     ((node.body, NodeAnno.BODY_SCOPE),
                                      (node.orelse, NodeAnno.ORELSE_SCOPE)))
exit(node)
