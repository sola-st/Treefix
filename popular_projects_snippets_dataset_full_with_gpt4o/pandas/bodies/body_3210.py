# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
# test does not blow up on length-0 DataFrame
zero_length = datetime_frame.reindex([])
result = zero_length.asfreq("BM")
assert result is not zero_length
