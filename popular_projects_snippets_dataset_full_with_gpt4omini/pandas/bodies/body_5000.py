# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
# GH-34740
from l3.Runtime import _l_
assert format(NA) == "<NA>"
_l_(10846)
assert format(NA, ">10") == "      <NA>"
_l_(10847)
assert format(NA, "xxx") == "<NA>"  # NA is flexible, accept any format spec
_l_(10848)  # NA is flexible, accept any format spec

assert f"{NA}" == "<NA>"
_l_(10849)
assert f"{NA:>10}" == "      <NA>"
_l_(10850)
assert f"{NA:xxx}" == "<NA>"
_l_(10851)
