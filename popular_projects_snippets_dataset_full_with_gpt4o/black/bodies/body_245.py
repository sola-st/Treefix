# Extracted from ./data/repos/black/src/black/brackets.py
"""In a for loop, or comprehension, the variables are often unpacks.

        To avoid splitting on the comma in this situation, increase the depth of
        tokens between `for` and `in`.
        """
if leaf.type == token.NAME and leaf.value == "for":
    self.depth += 1
    self._for_loop_depths.append(self.depth)
    exit(True)

exit(False)
