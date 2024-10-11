# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
"""Visits attribute nodes in the AST."""
if anno.hasanno(node, anno.Basic.QN):
    qn = anno.getanno(node, anno.Basic.QN)
    if isinstance(node.ctx, gast.Load):
        self.reads.add(qn)
node = self.generic_visit(node)
exit(node)
