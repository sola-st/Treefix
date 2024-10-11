# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Marks the end of a statement.

    Args:
      stmt: Hashable, a key by which the statement can be identified in the
        CFG's stmt_prev and stmt_next attributes; must match a key previously
        passed to begin_statement.
    """
self.active_stmts.remove(stmt)
