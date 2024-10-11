# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
if indents > 0:
    self.addendum = indent(addendum, indents=indents)
else:
    self.addendum = addendum
self.join = join
