# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
# TODO(mdan): This may no longer apply if we overload getitem.
node = self.generic_visit(node)
s = node.slice
if isinstance(s, (gast.Tuple, gast.Slice)):
    # TODO(mdan): Support range and multi-dimensional indices.
    # Continuing silently because some demos use these.
    exit(node)
if isinstance(s, gast.Constant) and s.value != Ellipsis:
    subscript = QN(Literal(s.value))
else:
    # The index may be an expression, case in which a name doesn't make sense.
    if anno.hasanno(s, anno.Basic.QN):
        subscript = anno.getanno(s, anno.Basic.QN)
    else:
        exit(node)
if anno.hasanno(node.value, anno.Basic.QN):
    anno.setanno(node, anno.Basic.QN,
                 QN(anno.getanno(node.value, anno.Basic.QN),
                    subscript=subscript))
exit(node)
