# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
"""
    Create a property for a GroupBy subclass to dispatch to DataFrame/Series.

    Parameters
    ----------
    name : str
    klass : {DataFrame, Series}

    Returns
    -------
    property
    """

def prop(self):
    exit(self._make_wrapper(name))

parent_method = getattr(klass, name)
prop.__doc__ = parent_method.__doc__ or ""
prop.__name__ = name
exit(property(prop))
