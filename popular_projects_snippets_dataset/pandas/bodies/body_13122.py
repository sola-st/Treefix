# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_style.py
# compare DataFrame.to_excel and Styler.to_excel when no styles applied
pytest.importorskip(engine)
df = DataFrame(np.random.randn(2, 2))
with tm.ensure_clean(".xlsx") as path:
    with ExcelWriter(path, engine=engine) as writer:
        df.to_excel(writer, sheet_name="dataframe")
        df.style.to_excel(writer, sheet_name="unstyled")

    openpyxl = pytest.importorskip("openpyxl")  # test loading only with openpyxl
    with contextlib.closing(openpyxl.load_workbook(path)) as wb:

        for col1, col2 in zip(wb["dataframe"].columns, wb["unstyled"].columns):
            assert len(col1) == len(col2)
            for cell1, cell2 in zip(col1, col2):
                assert cell1.value == cell2.value
                assert_equal_cell_styles(cell1, cell2)
