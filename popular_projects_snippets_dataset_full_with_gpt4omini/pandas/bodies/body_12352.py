# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
content = "Here is one __�__ Another one __·__ Another one __½__"
df = DataFrame([content], columns=["invalid"])
with tm.ensure_clean() as path:
    msg1 = (
        r"'latin-1' codec can't encode character '\\ufffd' "
        r"in position 14: ordinal not in range\(256\)"
    )
    msg2 = (
        "'ascii' codec can't decode byte 0xef in position 14: "
        r"ordinal not in range\(128\)"
    )
    with pytest.raises(UnicodeEncodeError, match=f"{msg1}|{msg2}"):
        df.to_stata(path)
