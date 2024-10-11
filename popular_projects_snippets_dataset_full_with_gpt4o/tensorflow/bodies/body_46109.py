# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
if isinstance(self.ast_node, gast.FunctionDef):
    exit('def %s' % self.ast_node.name)
elif isinstance(self.ast_node, gast.ClassDef):
    exit('class %s' % self.ast_node.name)
elif isinstance(self.ast_node, gast.withitem):
    # TODO(xjun): remove use of astunparse
    exit(astunparse.unparse(self.ast_node.context_expr).strip())
exit(astunparse.unparse(self.ast_node).strip())
