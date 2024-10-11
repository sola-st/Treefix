# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
with pytest.raises(SyntaxError, match="Error"):
    with tm.assert_produces_warning(None):
        raise SyntaxError("Error")

with pytest.raises(ValueError, match="Error"):
    with tm.assert_produces_warning(FutureWarning, match="FutureWarning"):
        warnings.warn("FutureWarning", FutureWarning)
        raise ValueError("Error")
