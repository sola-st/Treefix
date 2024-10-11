# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
df1 = DataFrame({"greeting": ["hello", "world"], "goodbye": ["goodbye", "people"]})
df2 = DataFrame(["poop"])

with tm.ensure_clean(ext) as f:
    df1.to_excel(f, engine="openpyxl", sheet_name="poo", index=False)
    with ExcelWriter(
        f, engine="openpyxl", mode="a", if_sheet_exists="overlay"
    ) as writer:
        # use startrow+1 because we don't have a header
        df2.to_excel(
            writer,
            index=False,
            header=False,
            startrow=startrow + 1,
            startcol=startcol,
            sheet_name="poo",
        )

    result = pd.read_excel(f, sheet_name="poo", engine="openpyxl")
    expected = DataFrame({"greeting": greeting, "goodbye": goodbye})
    tm.assert_frame_equal(result, expected)
