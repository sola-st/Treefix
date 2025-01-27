# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info.py
"""Adds origin information to an AST, based on the source it was loaded from.

  This allows us to map the original source code line numbers to generated
  source code.

  Note: the AST may be a part of a larger context (e.g. a function is part of
  a module that may contain other things). However, this function does not
  assume the source argument contains the entire context, nor that it contains
  only code corresponding to node itself. However, it assumes that node was
  parsed from the given source code.
  For this reason, two extra arguments are required, and they indicate the
  location of the node in the original context.

  Args:
    node: gast.AST, the AST to annotate.
    source: Text, the source code representing node.
    context_filepath: Text
    context_lineno: int
    context_col_offset: int
  """
# TODO(mdan): Pull this to a separate utility.
code_reader = io.StringIO(source)
comments_map = {}
try:
    for token in tokenize.generate_tokens(code_reader.readline):
        tok_type, tok_string, loc, _, _ = token
        srow, _ = loc
        if tok_type == tokenize.COMMENT:
            comments_map[srow] = tok_string.strip()[1:].strip()
except tokenize.TokenError:
    if isinstance(node, gast.Lambda):
        # Source code resolution in older Python versions is brittle for
        # lambda functions, and may contain garbage.
        pass
    else:
        raise

source_lines = source.split('\n')
visitor = OriginResolver(node, source_lines, comments_map,
                         context_lineno, context_col_offset,
                         context_filepath)
visitor.visit(node)
