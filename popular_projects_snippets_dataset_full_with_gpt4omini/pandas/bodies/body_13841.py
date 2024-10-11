# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 33562
cols = MultiIndex.from_product([["a", "b"], ["c", "d"], ["e", "f"]])
idxs = MultiIndex.from_product([["U", "V"], ["W", "X"], ["Y", "Z"]])
df = DataFrame(np.arange(64).reshape(8, 8), columns=cols, index=idxs)

for lvl in [0, 1]:
    key = slice_[lvl]
    if isinstance(key, tuple):
        for subkey in key:
            if isinstance(subkey, list) and "-" in subkey:
                # not present in the index level, raises KeyError since 2.0
                with pytest.raises(KeyError, match="-"):
                    df.loc[slice_]
                exit()

expected = df.loc[slice_]
result = df.loc[non_reducing_slice(slice_)]
tm.assert_frame_equal(result, expected)
