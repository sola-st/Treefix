# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

with tm.ensure_clean("__tmp_to_csv_from_csv1__") as path:
    float_frame.iloc[:5, float_frame.columns.get_loc("A")] = np.nan

    float_frame.to_csv(path)
    float_frame.to_csv(path, columns=["A", "B"])
    float_frame.to_csv(path, header=False)
    float_frame.to_csv(path, index=False)

    # test roundtrip
    # freq does not roundtrip
    datetime_frame.index = datetime_frame.index._with_freq(None)
    datetime_frame.to_csv(path)
    recons = self.read_csv(path, parse_dates=True)
    tm.assert_frame_equal(datetime_frame, recons)

    datetime_frame.to_csv(path, index_label="index")
    recons = self.read_csv(path, index_col=None, parse_dates=True)

    assert len(recons.columns) == len(datetime_frame.columns) + 1

    # no index
    datetime_frame.to_csv(path, index=False)
    recons = self.read_csv(path, index_col=None, parse_dates=True)
    tm.assert_almost_equal(datetime_frame.values, recons.values)

    # corner case
    dm = DataFrame(
        {
            "s1": Series(range(3), index=np.arange(3, dtype=np.int64)),
            "s2": Series(range(2), index=np.arange(2, dtype=np.int64)),
        }
    )
    dm.to_csv(path)

    recons = self.read_csv(path)
    tm.assert_frame_equal(dm, recons)
