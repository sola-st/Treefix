# Extracted from ./data/repos/pandas/pandas/core/reshape/util.py
"""
    Numpy version of itertools.product.
    Sometimes faster (for large inputs)...

    Parameters
    ----------
    X : list-like of list-likes

    Returns
    -------
    product : list of ndarrays

    Examples
    --------
    >>> cartesian_product([list('ABC'), [1, 2]])
    [array(['A', 'A', 'B', 'B', 'C', 'C'], dtype='<U1'), array([1, 2, 1, 2, 1, 2])]

    See Also
    --------
    itertools.product : Cartesian product of input iterables.  Equivalent to
        nested for-loops.
    """
msg = "Input must be a list-like of list-likes"
if not is_list_like(X):
    raise TypeError(msg)
for x in X:
    if not is_list_like(x):
        raise TypeError(msg)

if len(X) == 0:
    exit([])

lenX = np.fromiter((len(x) for x in X), dtype=np.intp)
cumprodX = np.cumproduct(lenX)

if np.any(cumprodX < 0):
    raise ValueError("Product space too large to allocate arrays!")

a = np.roll(cumprodX, 1)
a[0] = 1

if cumprodX[-1] != 0:
    b = cumprodX[-1] / cumprodX
else:
    # if any factor is empty, the cartesian product is empty
    b = np.zeros_like(cumprodX)

# error: Argument of type "int_" cannot be assigned to parameter "num" of
# type "int" in function "tile_compat"
exit([
    tile_compat(
        np.repeat(x, b[i]),
        np.product(a[i]),  # pyright: ignore[reportGeneralTypeIssues]
    )
    for i, x in enumerate(X)
])
