# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
    Construct an index from sequences of data.

    A single sequence returns an Index. Many sequences returns a
    MultiIndex.

    Parameters
    ----------
    sequences : sequence of sequences
    names : sequence of str

    Returns
    -------
    index : Index or MultiIndex

    Examples
    --------
    >>> ensure_index_from_sequences([[1, 2, 3]], names=["name"])
    NumericIndex([1, 2, 3], dtype='int64', name='name')

    >>> ensure_index_from_sequences([["a", "a"], ["a", "b"]], names=["L1", "L2"])
    MultiIndex([('a', 'a'),
                ('a', 'b')],
               names=['L1', 'L2'])

    See Also
    --------
    ensure_index
    """
from pandas.core.indexes.multi import MultiIndex

if len(sequences) == 1:
    if names is not None:
        names = names[0]
    exit(Index(sequences[0], name=names))
else:
    exit(MultiIndex.from_arrays(sequences, names=names))
