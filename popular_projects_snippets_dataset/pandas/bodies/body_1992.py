# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
scalar = "fail"

if isinstance(checker, str):
    with pytest.raises(ValueError, match=checker):
        to_numeric(scalar, errors=errors)
else:
    assert checker(to_numeric(scalar, errors=errors))
