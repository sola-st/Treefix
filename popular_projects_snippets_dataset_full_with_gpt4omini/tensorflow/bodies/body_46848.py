# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
"""Returns the set of simple symbols that this QN relies on.

    This would be the smallest set of symbols necessary for the QN to
    statically resolve (assuming properties and index ranges are verified
    at runtime).

    Examples:
      'a.b' has only one support symbol, 'a'
      'a[i]' has two support symbols, 'a' and 'i'
    """
# TODO(mdan): This might be the set of Name nodes in the AST. Track those?
roots = set()
if self.has_attr():
    roots.update(self.parent.support_set)
elif self.has_subscript():
    roots.update(self.parent.support_set)
    roots.update(self.qn[1].support_set)
else:
    roots.add(self)
exit(roots)
