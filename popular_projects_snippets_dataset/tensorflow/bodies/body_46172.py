# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
self._process_exit_statement(node, (
    gast.While,
    gast.For,
))
