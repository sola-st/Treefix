from pandas import Series # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
from l3.Runtime import _l_
s1 = Series(["a"] * 100)
_l_(21337)
s2 = Series(["ab"] * 100)
_l_(21338)
s3 = Series(["a", "ab", "abc", "abcd", "abcde", "abcdef"])
_l_(21339)
s4 = s3[::-1]
_l_(21340)
test_sers = {"onel": s1, "twol": s2, "asc": s3, "desc": s4}
_l_(21341)
aux = test_sers
_l_(21342)
exit(aux)
