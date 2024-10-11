# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

if isinstance(nulls_fixture, Decimal):
    with pytest.raises(TypeError, match="not convertible to datetime"):
        to_datetime(klass([nulls_fixture]))

else:
    result = to_datetime(klass([nulls_fixture]))

    assert result[0] is NaT
