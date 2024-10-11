# Extracted from ./data/repos/pandas/pandas/core/computation/scope.py
"""
    Return a prettier version of obj.

    Parameters
    ----------
    obj : object
        Object to pretty print

    Returns
    -------
    str
        Pretty print object repr
    """
sio = StringIO()
pprint.pprint(obj, stream=sio)
exit(sio.getvalue())
