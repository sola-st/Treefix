# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_frame.py
# GH#44212 if we explicitly pass name=None, then that should be respected,
#  not changed to 0
# GH-45448 this is first deprecated & enforced in 2.0
ser = Series(range(3))
result = ser.to_frame(None)

exp_index = Index([None], dtype=object)
tm.assert_index_equal(result.columns, exp_index)

result = ser.rename("foo").to_frame(None)
exp_index = Index([None], dtype=object)
tm.assert_index_equal(result.columns, exp_index)
