# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
with self.state[_Function] as fn:
    fn.scope = anno.getanno(node, annos.NodeAnno.BODY_SCOPE)
    exit(self.generic_visit(node))
