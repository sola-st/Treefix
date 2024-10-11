# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-12453
with tm.ensure_clean(ext) as path:
    df = DataFrame(
        {
            ("One", "x"): {0: 1},
            ("Two", "X"): {0: 3},
            ("Two", "Y"): {0: 7},
            ("Zero", ""): {0: 0},
        }
    )

    expected = DataFrame(
        {
            ("One", "x"): {0: 1},
            ("Two", "X"): {0: 3},
            ("Two", "Y"): {0: 7},
            ("Zero", "Unnamed: 4_level_1"): {0: 0},
        }
    )

    df.to_excel(path)
    actual = pd.read_excel(path, header=[0, 1], index_col=0)
    tm.assert_frame_equal(actual, expected)

    df = DataFrame(
        {
            ("Beg", ""): {0: 0},
            ("Middle", "x"): {0: 1},
            ("Tail", "X"): {0: 3},
            ("Tail", "Y"): {0: 7},
        }
    )

    expected = DataFrame(
        {
            ("Beg", "Unnamed: 1_level_1"): {0: 0},
            ("Middle", "x"): {0: 1},
            ("Tail", "X"): {0: 3},
            ("Tail", "Y"): {0: 7},
        }
    )

    df.to_excel(path)
    actual = pd.read_excel(path, header=[0, 1], index_col=0)
    tm.assert_frame_equal(actual, expected)
