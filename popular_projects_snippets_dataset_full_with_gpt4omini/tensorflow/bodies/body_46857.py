# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
node = self.generic_visit(node)
anno.setanno(node, anno.Basic.QN, QN(node.id))
exit(node)
