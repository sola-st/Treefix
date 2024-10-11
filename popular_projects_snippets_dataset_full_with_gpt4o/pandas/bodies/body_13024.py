# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 34748
if engine == "pyxlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )

f = "test_datetime_mi" + read_ext
with pd.ExcelFile(f) as excel:
    actual = pd.read_excel(excel, header=[0, 1], index_col=0, engine=engine)
expected_column_index = MultiIndex.from_tuples(
    [(pd.to_datetime("02/29/2020"), pd.to_datetime("03/01/2020"))],
    names=[
        pd.to_datetime("02/29/2020").to_pydatetime(),
        pd.to_datetime("03/01/2020").to_pydatetime(),
    ],
)
expected = DataFrame([], index=[], columns=expected_column_index)

tm.assert_frame_equal(expected, actual)
