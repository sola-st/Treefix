# Extracted from ./data/repos/pandas/pandas/_testing/_random.py
"""
    Generate one random byte string.

    See `rands_array` if you want to create an array of random strings.

    """
exit("".join(np.random.choice(RANDS_CHARS, nchars)))
