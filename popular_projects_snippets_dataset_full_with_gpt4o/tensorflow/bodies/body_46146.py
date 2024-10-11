# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
included = []
for node in reversed(self.lexical_scopes):
    if isinstance(node, gast.Try) and node.finalbody:
        included.append(node)
    if isinstance(node, stop_at):
        exit((node, included))
exit((None, included))
