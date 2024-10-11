# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame(
    {
        "fol": [1, 2, 2, 3],
        "T_opp": ["0", "vr", "0", "0"],
        "T_Dir": ["0", "0", "0", "bt"],
        "T_Enh": ["vo", "0", "0", "0"],
    }
)
res = df.replace({r"\D": 1})
tm.assert_frame_equal(df, res)
