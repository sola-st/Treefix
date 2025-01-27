# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# Enable Unicode option -----------------------------------------
with option_context("display.unicode.east_asian_width", True):

    # mid col
    df = DataFrame(
        {"a": ["あ", "いいい", "う", "ええええええ"], "b": [1, 222, 33333, 4]},
        index=["a", "bb", "c", "ddd"],
    )
    expected = (
        "                a      b\na              あ      1\n"
        "bb         いいい    222\nc              う  33333\n"
        "ddd  ええええええ      4"
    )
    assert repr(df) == expected

    # last col
    df = DataFrame(
        {"a": [1, 222, 33333, 4], "b": ["あ", "いいい", "う", "ええええええ"]},
        index=["a", "bb", "c", "ddd"],
    )
    expected = (
        "         a             b\na        1            あ\n"
        "bb     222        いいい\nc    33333            う\n"
        "ddd      4  ええええええ"
    )
    assert repr(df) == expected

    # all col
    df = DataFrame(
        {"a": ["あああああ", "い", "う", "えええ"], "b": ["あ", "いいい", "う", "ええええええ"]},
        index=["a", "bb", "c", "ddd"],
    )
    expected = (
        "              a             b\n"
        "a    あああああ            あ\n"
        "bb           い        いいい\n"
        "c            う            う\n"
        "ddd      えええ  ええええええ"
    )
    assert repr(df) == expected

    # column name
    df = DataFrame(
        {"b": ["あ", "いいい", "う", "ええええええ"], "あああああ": [1, 222, 33333, 4]},
        index=["a", "bb", "c", "ddd"],
    )
    expected = (
        "                b  あああああ\n"
        "a              あ           1\n"
        "bb         いいい         222\n"
        "c              う       33333\n"
        "ddd  ええええええ           4"
    )
    assert repr(df) == expected

    # index
    df = DataFrame(
        {"a": ["あああああ", "い", "う", "えええ"], "b": ["あ", "いいい", "う", "ええええええ"]},
        index=["あああ", "いいいいいい", "うう", "え"],
    )
    expected = (
        "                       a             b\n"
        "あああ        あああああ            あ\n"
        "いいいいいい          い        いいい\n"
        "うう                  う            う\n"
        "え                えええ  ええええええ"
    )
    assert repr(df) == expected

    # index name
    df = DataFrame(
        {"a": ["あああああ", "い", "う", "えええ"], "b": ["あ", "いいい", "う", "ええええええ"]},
        index=Index(["あ", "い", "うう", "え"], name="おおおお"),
    )
    expected = (
        "                   a             b\n"
        "おおおお                          \n"
        "あ        あああああ            あ\n"
        "い                い        いいい\n"
        "うう              う            う\n"
        "え            えええ  ええええええ"
    )
    assert repr(df) == expected

    # all
    df = DataFrame(
        {"あああ": ["あああ", "い", "う", "えええええ"], "いいいいい": ["あ", "いいい", "う", "ええ"]},
        index=Index(["あ", "いいい", "うう", "え"], name="お"),
    )
    expected = (
        "            あああ いいいいい\n"
        "お                           \n"
        "あ          あああ         あ\n"
        "いいい          い     いいい\n"
        "うう            う         う\n"
        "え      えええええ       ええ"
    )
    assert repr(df) == expected

    # MultiIndex
    idx = MultiIndex.from_tuples(
        [("あ", "いい"), ("う", "え"), ("おおお", "かかかか"), ("き", "くく")]
    )
    df = DataFrame(
        {"a": ["あああああ", "い", "う", "えええ"], "b": ["あ", "いいい", "う", "ええええええ"]},
        index=idx,
    )
    expected = (
        "                          a             b\n"
        "あ     いい      あああああ            あ\n"
        "う     え                い        いいい\n"
        "おおお かかかか          う            う\n"
        "き     くく          えええ  ええええええ"
    )
    assert repr(df) == expected

    # truncate
    with option_context("display.max_rows", 3, "display.max_columns", 3):

        df = DataFrame(
            {
                "a": ["あああああ", "い", "う", "えええ"],
                "b": ["あ", "いいい", "う", "ええええええ"],
                "c": ["お", "か", "ききき", "くくくくくく"],
                "ああああ": ["さ", "し", "す", "せ"],
            },
            columns=["a", "b", "c", "ああああ"],
        )

        expected = (
            "             a  ... ああああ\n"
            "0   あああああ  ...       さ\n"
            "..         ...  ...      ...\n"
            "3       えええ  ...       せ\n"
            "\n[4 rows x 4 columns]"
        )
        assert repr(df) == expected

        df.index = ["あああ", "いいいい", "う", "aaa"]
        expected = (
            "                 a  ... ああああ\n"
            "あああ  あああああ  ...       さ\n"
            "...            ...  ...      ...\n"
            "aaa         えええ  ...       せ\n"
            "\n[4 rows x 4 columns]"
        )
        assert repr(df) == expected

    # ambiguous unicode
    df = DataFrame(
        {"b": ["あ", "いいい", "¡¡", "ええええええ"], "あああああ": [1, 222, 33333, 4]},
        index=["a", "bb", "c", "¡¡¡"],
    )
    expected = (
        "                b  あああああ\n"
        "a              あ           1\n"
        "bb         いいい         222\n"
        "c              ¡¡       33333\n"
        "¡¡¡  ええええええ           4"
    )
    assert repr(df) == expected
