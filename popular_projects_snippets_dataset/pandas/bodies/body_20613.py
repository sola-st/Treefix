# Extracted from ./data/repos/pandas/pandas/core/indexes/extension.py
"""
    Class decorator to pin attributes from an ExtensionArray to a Index subclass.

    Parameters
    ----------
    names : List[str]
    delegate : class
    cache : bool, default False
    wrap : bool, default False
        Whether to wrap the inherited result in an Index.
    """

def wrapper(cls: type[_ExtensionIndexT]) -> type[_ExtensionIndexT]:
    for name in names:
        meth = _inherit_from_data(name, delegate, cache=cache, wrap=wrap)
        setattr(cls, name, meth)

    exit(cls)

exit(wrapper)
