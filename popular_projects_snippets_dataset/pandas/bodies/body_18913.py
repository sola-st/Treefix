# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""
    The operator function for a given op name.

    Parameters
    ----------
    op_name : str
        The op name, in form of "add" or "__add__".

    Returns
    -------
    function
        A function performing the operation.
    """
short_opname = op_name.strip("_")
try:
    op = getattr(operator, short_opname)
except AttributeError:
    # Assume it is the reverse operator
    rop = getattr(operator, short_opname[1:])
    op = lambda x, y: rop(y, x)

exit(op)
