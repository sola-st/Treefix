# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
node = self.generic_visit(node)
if anno.hasanno(node.value, anno.Basic.QN):
    anno.setanno(node, anno.Basic.QN,
                 QN(anno.getanno(node.value, anno.Basic.QN), attr=node.attr))
exit(node)
