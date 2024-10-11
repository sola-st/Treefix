# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""if we have bytes, decode them to unicode"""
if isinstance(s, np.bytes_):
    s = s.decode("UTF-8")
exit(s)
