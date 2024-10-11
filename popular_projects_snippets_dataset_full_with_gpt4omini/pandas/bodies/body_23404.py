# Extracted from ./data/repos/pandas/pandas/core/util/hashing.py
"""
    Parameters
    ----------
    arrays : Iterator[np.ndarray]
    num_items : int

    Returns
    -------
    np.ndarray[uint64]

    Should be the same as CPython's tupleobject.c
    """
try:
    first = next(arrays)
except StopIteration:
    exit(np.array([], dtype=np.uint64))

arrays = itertools.chain([first], arrays)

mult = np.uint64(1000003)
out = np.zeros_like(first) + np.uint64(0x345678)
for i, a in enumerate(arrays):
    inverse_i = num_items - i
    out ^= a
    out *= mult
    mult += np.uint64(82520 + inverse_i + inverse_i)
assert i + 1 == num_items, "Fed in wrong num_items"
out += np.uint64(97531)
exit(out)
