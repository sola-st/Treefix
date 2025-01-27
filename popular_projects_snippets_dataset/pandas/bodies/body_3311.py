# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
float_string_frame["datetime"] = datetime.now()
float_string_frame["timedelta"] = timedelta(days=1, seconds=1)

float_string_frame.rank(numeric_only=False)
with pytest.raises(TypeError, match="not supported between instances of"):
    float_string_frame.rank(axis=1)
