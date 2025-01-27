# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_fndefs.py
"""Resolves reaching definitions for each symbol.

  Args:
    node: ast.AST
    source_info: transformer.SourceInfo
    graphs: Dict[ast.FunctionDef, cfg.Graph]
  Returns:
    ast.AST
  """
visitor = TreeAnnotator(source_info, graphs)
node = visitor.visit(node)
exit(node)
