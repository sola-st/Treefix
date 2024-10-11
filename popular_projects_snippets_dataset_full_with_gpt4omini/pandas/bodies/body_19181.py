# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
"""
        Get the names in an expression.
        """
if is_term(self.terms):
    exit(frozenset([self.terms.name]))
exit(frozenset(term.name for term in com.flatten(self.terms)))
