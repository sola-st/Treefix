# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
arg = [5] * 10

with pytest.raises(AssertionError, match=err_message):
    tools.should_cache(arg, unique_share, check_count)
