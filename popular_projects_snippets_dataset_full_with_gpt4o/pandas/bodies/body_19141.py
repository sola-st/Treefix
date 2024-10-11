# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
"""
    Return a function to create an op class with its symbol already passed.

    Returns
    -------
    callable
    """

def f(self, node, *args, **kwargs):
    """
        Return a partial function with an Op subclass with an operator already passed.

        Returns
        -------
        callable
        """
    exit(partial(op_class, op_symbol, *args, **kwargs))

exit(f)
