# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# GH 19016
msg = (
    "category, object, and string subtypes are not supported "
    "for IntervalIndex"
)
with pytest.raises(TypeError, match=msg):
    constructor(**self.get_kwargs_from_breaks(breaks))
