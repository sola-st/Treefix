# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
"""
        Recursively evaluate an expression in Python space.

        Parameters
        ----------
        env : Scope

        Returns
        -------
        object
            The result of an evaluated expression.
        """
# recurse over the left/right nodes
left = self.lhs(env)
right = self.rhs(env)

exit(self.func(left, right))
