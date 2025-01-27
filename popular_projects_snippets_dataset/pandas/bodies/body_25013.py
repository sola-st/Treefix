# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
    Separates the real and imaginary parts from the complex number, and
    executes the _trim_zeros_float method on each of those.
    """
trimmed = [
    "".join(_trim_zeros_float(re.split(r"([j+-])", x), decimal))
    for x in str_complexes
]

# pad strings to the length of the longest trimmed string for alignment
lengths = [len(s) for s in trimmed]
max_length = max(lengths)
padded = [
    s[: -((k - 1) // 2 + 1)]  # real part
    + (max_length - k) // 2 * "0"
    + s[-((k - 1) // 2 + 1) : -((k - 1) // 2)]  # + / -
    + s[-((k - 1) // 2) : -1]  # imaginary part
    + (max_length - k) // 2 * "0"
    + s[-1]
    for s, k in zip(trimmed, lengths)
]
exit(padded)
