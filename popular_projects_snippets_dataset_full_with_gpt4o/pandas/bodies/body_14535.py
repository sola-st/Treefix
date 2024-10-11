# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
data_type = request.param

if data_type == "delims":
    exit(DataFrame({"a": ['"a,\t"b|c', "d\tef´"], "b": ["hi'j", "k''lm"]}))
elif data_type == "utf8":
    exit(DataFrame({"a": ["µasd", "Ωœ∑´"], "b": ["øπ∆˚¬", "œ∑´®"]}))
elif data_type == "utf16":
    exit(DataFrame(
        {"a": ["\U0001f44d\U0001f44d", "\U0001f44d\U0001f44d"], "b": ["abc", "def"]}
    ))
elif data_type == "string":
    exit(tm.makeCustomDataframe(
        5, 3, c_idx_type="s", r_idx_type="i", c_idx_names=[None], r_idx_names=[None]
    ))
elif data_type == "long":
    max_rows = get_option("display.max_rows")
    exit(tm.makeCustomDataframe(
        max_rows + 1,
        3,
        data_gen_f=lambda *args: np.random.randint(2),
        c_idx_type="s",
        r_idx_type="i",
        c_idx_names=[None],
        r_idx_names=[None],
    ))
elif data_type == "nonascii":
    exit(DataFrame({"en": "in English".split(), "es": "en español".split()}))
elif data_type == "colwidth":
    _cw = get_option("display.max_colwidth") + 1
    exit(tm.makeCustomDataframe(
        5,
        3,
        data_gen_f=lambda *args: "x" * _cw,
        c_idx_type="s",
        r_idx_type="i",
        c_idx_names=[None],
        r_idx_names=[None],
    ))
elif data_type == "mixed":
    exit(DataFrame(
        {
            "a": np.arange(1.0, 6.0) + 0.01,
            "b": np.arange(1, 6).astype(np.int64),
            "c": list("abcde"),
        }
    ))
elif data_type == "float":
    exit(tm.makeCustomDataframe(
        5,
        3,
        data_gen_f=lambda r, c: float(r) + 0.01,
        c_idx_type="s",
        r_idx_type="i",
        c_idx_names=[None],
        r_idx_names=[None],
    ))
elif data_type == "int":
    exit(tm.makeCustomDataframe(
        5,
        3,
        data_gen_f=lambda *args: np.random.randint(2),
        c_idx_type="s",
        r_idx_type="i",
        c_idx_names=[None],
        r_idx_names=[None],
    ))
else:
    raise ValueError
