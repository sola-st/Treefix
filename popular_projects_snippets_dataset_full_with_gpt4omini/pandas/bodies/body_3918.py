# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH-28301
df = DataFrame(index=index, columns=columns).fillna(1)
stacked = df.stack()
new_index = MultiIndex.from_tuples(stacked.index.to_numpy())
expected = DataFrame(
    stacked.to_numpy(), index=new_index, columns=stacked.columns
)
tm.assert_frame_equal(stacked, expected)
stacked_codes = np.asarray(stacked.index.codes)
expected_codes = np.asarray(new_index.codes)
tm.assert_numpy_array_equal(stacked_codes, expected_codes)
