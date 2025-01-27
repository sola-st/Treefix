# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
"""Visits nodes with subscript in the AST."""
s = node.slice
if anno.hasanno(node, anno.Basic.QN):
    qn = anno.getanno(node, anno.Basic.QN)
    if isinstance(node.ctx, gast.Load):
        self.reads.add(qn)
elif isinstance(s, (gast.Tuple, gast.Slice)):
    if anno.hasanno(node.value, anno.Basic.QN):
        self.complex_reads.add(anno.getanno(node.value, anno.Basic.QN))
value_qn = anno.getanno(node.value, anno.Basic.QN, None)
if value_qn in self.exclude:
    node.value = self.generic_visit(node.value)
else:
    node.value = self.visit(node.value)
node.slice = self.visit(s)
exit(node)
