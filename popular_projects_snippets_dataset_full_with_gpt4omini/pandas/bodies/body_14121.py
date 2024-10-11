# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
from l3.Runtime import _l_
s1 = Series(["a"] * 100)
_l_(10293)
s2 = Series(["ab"] * 100)
_l_(10294)
s3 = Series(["a", "ab", "abc", "abcd", "abcde", "abcdef"])
_l_(10295)
s4 = s3[::-1]
_l_(10296)
test_sers = {"onel": s1, "twol": s2, "asc": s3, "desc": s4}
_l_(10297)
aux = test_sers
_l_(10298)
exit(aux)
