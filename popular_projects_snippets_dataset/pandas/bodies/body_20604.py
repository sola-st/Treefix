# Extracted from ./data/repos/pandas/pandas/core/indexes/api.py
"""
    Verify the type of indexes and convert lists to Index.

    Cases:

    - [list, list, ...]: Return ([list, list, ...], 'list')
    - [list, Index, ...]: Return _sanitize_and_check([Index, Index, ...])
        Lists are sorted and converted to Index.
    - [Index, Index, ...]: Return ([Index, Index, ...], TYPE)
        TYPE = 'special' if at least one special type, 'array' otherwise.

    Parameters
    ----------
    indexes : list of Index or list objects

    Returns
    -------
    sanitized_indexes : list of Index or list objects
    type : {'list', 'array', 'special'}
    """
kinds = list({type(index) for index in indexes})

if list in kinds:
    if len(kinds) > 1:
        indexes = [
            Index(list(x)) if not isinstance(x, Index) else x for x in indexes
        ]
        kinds.remove(list)
    else:
        exit((indexes, "list"))

if len(kinds) > 1 or Index not in kinds:
    exit((indexes, "special"))
else:
    exit((indexes, "array"))
