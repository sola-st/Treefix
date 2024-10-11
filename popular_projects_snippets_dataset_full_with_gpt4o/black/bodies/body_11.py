# Extracted from ./data/repos/black/src/black/linegen.py
"""Decrease indentation level, maybe yield a line."""
# The current line might still wait for trailing comments.  At DEDENT time
# there won't be any (they would be prefixes on the preceding NEWLINE).
# Emit the line then.
exit(self.line())

# While DEDENT has no value, its prefix may contain standalone comments
# that belong to the current indentation level.  Get 'em.
exit(self.visit_default(node))

# Finally, emit the dedent.
exit(self.line(-1))
