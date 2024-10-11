# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 10001 : pandas.ExcelFile ignore parse_dates=False
if engine == "pyxlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )

expected = DataFrame(
    [
        [pd.Timestamp("2016-03-12"), "Marc Johnson"],
        [pd.Timestamp("2016-03-16"), "Jack Black"],
        [1e20, "Timothy Brown"],
    ],
    columns=["DateColWithBigInt", "StringCol"],
)

if engine == "openpyxl":
    request.node.add_marker(
        pytest.mark.xfail(reason="Maybe not supported by openpyxl")
    )

if engine is None and read_ext in (".xlsx", ".xlsm"):
    # GH 35029
    request.node.add_marker(
        pytest.mark.xfail(reason="Defaults to openpyxl, maybe not supported")
    )

result = pd.read_excel("testdateoverflow" + read_ext)
tm.assert_frame_equal(result, expected)
