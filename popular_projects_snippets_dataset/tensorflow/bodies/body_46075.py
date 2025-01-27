# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
if node.arg not in self.replacements:
    exit(self.generic_visit(node))

repl = self._prepare_replacement(node, node.arg)
if isinstance(repl, gast.keyword):
    exit(repl)
elif (repl and isinstance(repl, (list, tuple)) and
      all(isinstance(r, gast.keyword) for r in repl)):
    exit(repl)
# TODO(mdan): We may allow replacing with a string as well.
# For example, if one wanted to replace foo with bar in foo=baz, then
# we could allow changing just node arg, so that we end up with bar=baz.
raise ValueError(
    'a keyword argument may only be replaced by another keyword or a '
    'non-empty list of keywords. Found: {} for keyword {}'.format(
        repl, node.arg))
