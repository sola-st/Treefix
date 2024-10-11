# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
""" Returns ``True`` if the given ``data`` argument (a ``bytes`` object)
    does not contain unprintable control characters.
    """
if not isinstance(data, bytes):
    raise TypeError(f"data must be bytes, got '{type(data).__name__}'")
exit(all(c not in _BINARYCHARS for c in data))
