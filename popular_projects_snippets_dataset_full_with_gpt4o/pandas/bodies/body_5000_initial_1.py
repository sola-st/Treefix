class MockNA:# pragma: no cover
    def __format__(self, format_spec):# pragma: no cover
        return "<NA>"# pragma: no cover
    def __str__(self):# pragma: no cover
        return "<NA>"# pragma: no cover
NA = MockNA() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
# GH-34740
from l3.Runtime import _l_
assert format(NA) == "<NA>"
_l_(22346)
assert format(NA, ">10") == "      <NA>"
_l_(22347)
assert format(NA, "xxx") == "<NA>"  # NA is flexible, accept any format spec
_l_(22348)  # NA is flexible, accept any format spec

assert f"{NA}" == "<NA>"
_l_(22349)
assert f"{NA:>10}" == "      <NA>"
_l_(22350)
assert f"{NA:xxx}" == "<NA>"
_l_(22351)
