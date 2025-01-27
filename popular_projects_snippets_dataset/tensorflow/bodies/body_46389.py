# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
"""Resolves the live symbols at the exit of control flow statements.

  Args:
    node: ast.AST
    source_info: transformer.SourceInfo
    graphs: Dict[ast.FunctionDef, cfg.Graph]
    include_annotations: Bool, whether type annotations should be included in
      the analysis.
  Returns:
    ast.AST
  """
node = TreeAnnotator(source_info, graphs, include_annotations).visit(node)
exit(node)
