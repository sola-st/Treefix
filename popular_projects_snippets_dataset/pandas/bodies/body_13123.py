# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_style.py
pytest.importorskip(engine)
df = DataFrame(np.random.randn(1, 1))
styler = df.style.applymap(lambda x: css)

with tm.ensure_clean(".xlsx") as path:
    with ExcelWriter(path, engine=engine) as writer:
        df.to_excel(writer, sheet_name="dataframe")
        styler.to_excel(writer, sheet_name="styled")

    openpyxl = pytest.importorskip("openpyxl")  # test loading only with openpyxl
    with contextlib.closing(openpyxl.load_workbook(path)) as wb:

        # test unstyled data cell does not have expected styles
        # test styled cell has expected styles
        u_cell, s_cell = wb["dataframe"].cell(2, 2), wb["styled"].cell(2, 2)
    for attr in attrs:
        u_cell, s_cell = getattr(u_cell, attr, None), getattr(s_cell, attr)

    if isinstance(expected, dict):
        assert u_cell is None or u_cell != expected[engine]
        assert s_cell == expected[engine]
    else:
        assert u_cell is None or u_cell != expected
        assert s_cell == expected
