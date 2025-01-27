# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
included = []
for node in reversed(self.lexical_scopes):
    if isinstance(node, gast.Try) and node.handlers:
        included.extend(node.handlers)
    if isinstance(node, stop_at):
        break
exit(included)
