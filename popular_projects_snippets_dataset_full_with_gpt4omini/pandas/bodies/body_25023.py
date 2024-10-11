# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
    Appends lines to a buffer.

    Parameters
    ----------
    buf
        The buffer to write to
    lines
        The lines to append.
    """
if any(isinstance(x, str) for x in lines):
    lines = [str(x) for x in lines]
buf.write("\n".join(lines))
