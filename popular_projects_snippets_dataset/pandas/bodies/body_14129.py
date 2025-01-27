# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# not aligned properly because of east asian width

# unicode index
s = Series(["a", "bb", "CCC", "D"], index=["あ", "いい", "ううう", "ええええ"])
expected = "あ         a\nいい       bb\nううう     CCC\nええええ      D\ndtype: object"
assert repr(s) == expected

# unicode values
s = Series(["あ", "いい", "ううう", "ええええ"], index=["a", "bb", "c", "ddd"])
expected = "a         あ\nbb       いい\nc       ううう\nddd    ええええ\ndtype: object"
assert repr(s) == expected

# both
s = Series(["あ", "いい", "ううう", "ええええ"], index=["ああ", "いいいい", "う", "えええ"])
expected = (
    "ああ         あ\nいいいい      いい\nう        ううう\nえええ     ええええ\ndtype: object"
)
assert repr(s) == expected

# unicode footer
s = Series(
    ["あ", "いい", "ううう", "ええええ"], index=["ああ", "いいいい", "う", "えええ"], name="おおおおおおお"
)
expected = (
    "ああ         あ\nいいいい      いい\nう        ううう\n"
    "えええ     ええええ\nName: おおおおおおお, dtype: object"
)
assert repr(s) == expected

# MultiIndex
idx = MultiIndex.from_tuples(
    [("あ", "いい"), ("う", "え"), ("おおお", "かかかか"), ("き", "くく")]
)
s = Series([1, 22, 3333, 44444], index=idx)
expected = (
    "あ    いい          1\n"
    "う    え          22\n"
    "おおお  かかかか     3333\n"
    "き    くく      44444\ndtype: int64"
)
assert repr(s) == expected

# object dtype, shorter than unicode repr
s = Series([1, 22, 3333, 44444], index=[1, "AB", np.nan, "あああ"])
expected = (
    "1          1\nAB        22\nNaN     3333\nあああ    44444\ndtype: int64"
)
assert repr(s) == expected

# object dtype, longer than unicode repr
s = Series(
    [1, 22, 3333, 44444], index=[1, "AB", Timestamp("2011-01-01"), "あああ"]
)
expected = (
    "1                          1\n"
    "AB                        22\n"
    "2011-01-01 00:00:00     3333\n"
    "あああ                    44444\ndtype: int64"
)
assert repr(s) == expected

# truncate
with option_context("display.max_rows", 3):
    s = Series(["あ", "いい", "ううう", "ええええ"], name="おおおおおおお")

    expected = (
        "0       あ\n     ... \n"
        "3    ええええ\n"
        "Name: おおおおおおお, Length: 4, dtype: object"
    )
    assert repr(s) == expected

    s.index = ["ああ", "いいいい", "う", "えええ"]
    expected = (
        "ああ        あ\n       ... \n"
        "えええ    ええええ\n"
        "Name: おおおおおおお, Length: 4, dtype: object"
    )
    assert repr(s) == expected

# Enable Unicode option -----------------------------------------
with option_context("display.unicode.east_asian_width", True):

    # unicode index
    s = Series(["a", "bb", "CCC", "D"], index=["あ", "いい", "ううう", "ええええ"])
    expected = (
        "あ            a\nいい         bb\nううう      CCC\n"
        "ええええ      D\ndtype: object"
    )
    assert repr(s) == expected

    # unicode values
    s = Series(["あ", "いい", "ううう", "ええええ"], index=["a", "bb", "c", "ddd"])
    expected = (
        "a            あ\nbb         いい\nc        ううう\n"
        "ddd    ええええ\ndtype: object"
    )
    assert repr(s) == expected

    # both
    s = Series(["あ", "いい", "ううう", "ええええ"], index=["ああ", "いいいい", "う", "えええ"])
    expected = (
        "ああ              あ\n"
        "いいいい        いい\n"
        "う            ううう\n"
        "えええ      ええええ\ndtype: object"
    )
    assert repr(s) == expected

    # unicode footer
    s = Series(
        ["あ", "いい", "ううう", "ええええ"],
        index=["ああ", "いいいい", "う", "えええ"],
        name="おおおおおおお",
    )
    expected = (
        "ああ              あ\n"
        "いいいい        いい\n"
        "う            ううう\n"
        "えええ      ええええ\n"
        "Name: おおおおおおお, dtype: object"
    )
    assert repr(s) == expected

    # MultiIndex
    idx = MultiIndex.from_tuples(
        [("あ", "いい"), ("う", "え"), ("おおお", "かかかか"), ("き", "くく")]
    )
    s = Series([1, 22, 3333, 44444], index=idx)
    expected = (
        "あ      いい            1\n"
        "う      え             22\n"
        "おおお  かかかか     3333\n"
        "き      くく        44444\n"
        "dtype: int64"
    )
    assert repr(s) == expected

    # object dtype, shorter than unicode repr
    s = Series([1, 22, 3333, 44444], index=[1, "AB", np.nan, "あああ"])
    expected = (
        "1             1\nAB           22\nNaN        3333\n"
        "あああ    44444\ndtype: int64"
    )
    assert repr(s) == expected

    # object dtype, longer than unicode repr
    s = Series(
        [1, 22, 3333, 44444],
        index=[1, "AB", Timestamp("2011-01-01"), "あああ"],
    )
    expected = (
        "1                          1\n"
        "AB                        22\n"
        "2011-01-01 00:00:00     3333\n"
        "あああ                 44444\ndtype: int64"
    )
    assert repr(s) == expected

    # truncate
    with option_context("display.max_rows", 3):
        s = Series(["あ", "いい", "ううう", "ええええ"], name="おおおおおおお")
        expected = (
            "0          あ\n       ...   \n"
            "3    ええええ\n"
            "Name: おおおおおおお, Length: 4, dtype: object"
        )
        assert repr(s) == expected

        s.index = ["ああ", "いいいい", "う", "えええ"]
        expected = (
            "ああ            あ\n"
            "            ...   \n"
            "えええ    ええええ\n"
            "Name: おおおおおおお, Length: 4, dtype: object"
        )
        assert repr(s) == expected

    # ambiguous unicode
    s = Series(
        ["¡¡", "い¡¡", "ううう", "ええええ"], index=["ああ", "¡¡¡¡いい", "¡¡", "えええ"]
    )
    expected = (
        "ああ              ¡¡\n"
        "¡¡¡¡いい        い¡¡\n"
        "¡¡            ううう\n"
        "えええ      ええええ\ndtype: object"
    )
    assert repr(s) == expected
