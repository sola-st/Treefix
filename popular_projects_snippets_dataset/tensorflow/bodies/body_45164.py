# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives.py
if self.state[_LoopScope].statements_visited > 1:
    raise ValueError(
        '"%s" must be the first statement in the loop block' % (
            directive.__name__))
if self.state[_LoopScope].level < 2:
    raise ValueError(
        '"%s" must be used inside a statement' % directive.__name__)
target = self.state[_LoopScope].ast_node
node_anno = anno.getanno(target, anno.Basic.DIRECTIVES, {})
node_anno[directive] = _map_args(call_node, directive)
anno.setanno(target, anno.Basic.DIRECTIVES, node_anno)
exit(call_node)
