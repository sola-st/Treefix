# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
if isinstance(fn_ast_node, gast.Lambda):
    # Exception: lambda functions are assumed to be used only in the
    # place where they are defined, and not later.
    exit(True)
exit(False)
