# Extracted from ./data/repos/pandas/pandas/_testing/_random.py
"""
    Generate an array of byte strings.
    """
retval = (
    np.random.choice(RANDS_CHARS, size=nchars * np.prod(size), replace=replace)
    .view((np.str_, nchars))
    .reshape(size)
)
exit(retval.astype(dtype))
