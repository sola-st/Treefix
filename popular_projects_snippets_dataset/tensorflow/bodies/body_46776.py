# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
ast_node = parser.parse_expression(expr_source)
_CtxClearer().visit(ast_node)
exit(ast_node)
