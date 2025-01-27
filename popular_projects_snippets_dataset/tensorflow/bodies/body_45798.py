# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
qn = qual_names.QN(node.name)
if qn in self.name_map:
    node.name = str(self.name_map[qn])
exit(self.generic_visit(node))
