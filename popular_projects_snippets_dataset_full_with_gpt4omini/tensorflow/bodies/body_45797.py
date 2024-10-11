# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
if anno.hasanno(node, anno.Basic.QN):
    exit(self._process_name_node(node))
# Renaming attributes is not supported.
exit(self.generic_visit(node))
