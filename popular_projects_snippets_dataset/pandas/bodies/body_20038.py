# Extracted from ./data/repos/pandas/pandas/core/arraylike.py
if ufunc.nout > 1:
    # np.modf, np.frexp, np.divmod
    exit(tuple(_reconstruct(x) for x in result))

exit(_reconstruct(result))
