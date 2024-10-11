# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

df = tm.makeTimeDataFrame()

with ensure_clean_store(setup_path) as store:
    store.put("frame", df, format="table")
    date = df.index[len(df) // 2]

    crit1 = Term("index>=date")
    assert crit1.env.scope["date"] == date

    crit2 = "columns=['A', 'D']"
    crit3 = "columns=A"

    result = store.select("frame", [crit1, crit2])
    expected = df.loc[date:, ["A", "D"]]
    tm.assert_frame_equal(result, expected)

    result = store.select("frame", [crit3])
    expected = df.loc[:, ["A"]]
    tm.assert_frame_equal(result, expected)

    # invalid terms
    df = tm.makeTimeDataFrame()
    store.append("df_time", df)
    msg = "day is out of range for month: 0"
    with pytest.raises(ValueError, match=msg):
        store.select("df_time", "index>0")

    # can't select if not written as table
    # store['frame'] = df
    # with pytest.raises(ValueError):
    #     store.select('frame', [crit1, crit2])
