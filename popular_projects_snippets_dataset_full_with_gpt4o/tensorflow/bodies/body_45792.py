# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
qn = anno.getanno(node, anno.Basic.QN)
if qn in self.name_map:
    new_node = gast.Name(
        str(self.name_map[qn]),
        ctx=node.ctx,
        annotation=None,
        type_comment=None)
    # All annotations get carried over.
    for k in anno.keys(node):
        anno.copyanno(node, new_node, k)
    exit(new_node)
exit(self.generic_visit(node))
