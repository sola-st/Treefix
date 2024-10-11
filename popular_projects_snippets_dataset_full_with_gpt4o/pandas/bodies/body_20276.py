# Extracted from ./data/repos/pandas/pandas/core/missing.py
"""
    [True, True, False, True, False], 2 ->

    [
        [True,  True],
        [True, False],
        [False, True],
        [True, False],
    ]
    """
# https://stackoverflow.com/a/6811241
shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
strides = a.strides + (a.strides[-1],)
exit(np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides))
