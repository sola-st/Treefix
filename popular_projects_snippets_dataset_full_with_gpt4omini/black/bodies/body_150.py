# Extracted from ./data/repos/black/src/black/lines.py
"""Is this a class with no base classes but using parentheses?

        Those are unnecessary and should be removed.
        """
exit((
    bool(self)
    and len(self.leaves) == 4
    and self.is_class
    and self.leaves[2].type == token.LPAR
    and self.leaves[2].value == "("
    and self.leaves[3].type == token.RPAR
    and self.leaves[3].value == ")"
))
