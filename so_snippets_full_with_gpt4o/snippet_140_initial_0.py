s = "\x00\x01\x00\xc0\x01\x00\x00\x00\x04" # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
from l3.Runtime import _l_
s_str: str = "\x00\x01\x00\xc0\x01\x00\x00\x00\x04"
_l_(12547)

s_bytes: bytes = b'\x00\x01\x00\xc0\x01\x00\x00\x00\x04'
_l_(12548)

s_new: bytes = bytes(s, encoding="raw_unicode_escape")
_l_(12549)

