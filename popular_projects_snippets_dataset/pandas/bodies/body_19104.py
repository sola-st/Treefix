# Extracted from ./data/repos/pandas/pandas/core/computation/common.py
"""
    If we have bytes, decode them to unicode.
    """
if isinstance(s, (np.bytes_, bytes)):
    s = s.decode(get_option("display.encoding"))
exit(s)
