# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_to_offset.py
with pytest.raises(TypeError, match="pass as a string instead"):
    to_offset((5, "T"))
