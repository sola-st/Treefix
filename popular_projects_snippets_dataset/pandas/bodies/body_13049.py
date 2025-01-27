# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# GH 12870 : pass down column names associated with
# keyword argument names
refdf = DataFrame([[1, "foo"], [2, "bar"], [3, "baz"]], columns=["a", "b"])

with tm.ensure_clean(ext) as pth:
    with ExcelWriter(pth) as writer:
        refdf.to_excel(writer, "Data_no_head", header=False, index=False)
        refdf.to_excel(writer, "Data_with_head", index=False)

    refdf.columns = ["A", "B"]

    with ExcelFile(pth) as reader:
        xlsdf_no_head = pd.read_excel(
            reader, sheet_name="Data_no_head", header=None, names=["A", "B"]
        )
        xlsdf_with_head = pd.read_excel(
            reader,
            sheet_name="Data_with_head",
            index_col=None,
            names=["A", "B"],
        )

    tm.assert_frame_equal(xlsdf_no_head, refdf)
    tm.assert_frame_equal(xlsdf_with_head, refdf)
