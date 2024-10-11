# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
self._enter_scope(False)
node.target = self.visit(node.target)
node.iter = self.visit(node.iter)
self._exit_and_record_scope(node.iter)

self._enter_scope(False)
self.visit(node.target)
if anno.hasanno(node, anno.Basic.EXTRA_LOOP_TEST):
    self._process_statement(anno.getanno(node, anno.Basic.EXTRA_LOOP_TEST))
self._exit_and_record_scope(node, tag=NodeAnno.ITERATE_SCOPE)

node = self._process_parallel_blocks(node,
                                     ((node.body, NodeAnno.BODY_SCOPE),
                                      (node.orelse, NodeAnno.ORELSE_SCOPE)))
exit(node)
