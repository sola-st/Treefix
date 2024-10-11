# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_style.py
pytest.importorskip(engine)
df = DataFrame(np.random.randn(1, 1))

styler = df.style
styler.applymap_index(lambda x: css, axis=0)
styler.applymap_index(lambda x: css, axis=1)

null_styler = df.style
null_styler.applymap(lambda x: "null: css;")
null_styler.applymap_index(lambda x: "null: css;", axis=0)
null_styler.applymap_index(lambda x: "null: css;", axis=1)

with tm.ensure_clean(".xlsx") as path:
    with ExcelWriter(path, engine=engine) as writer:
        null_styler.to_excel(writer, sheet_name="null_styled")
        styler.to_excel(writer, sheet_name="styled")

    openpyxl = pytest.importorskip("openpyxl")  # test loading only with openpyxl
    with contextlib.closing(openpyxl.load_workbook(path)) as wb:

        # test null styled index cells does not have expected styles
        # test styled cell has expected styles
        ui_cell, si_cell = wb["null_styled"].cell(2, 1), wb["styled"].cell(2, 1)
        uc_cell, sc_cell = wb["null_styled"].cell(1, 2), wb["styled"].cell(1, 2)
    for attr in attrs:
        ui_cell, si_cell = getattr(ui_cell, attr, None), getattr(si_cell, attr)
        uc_cell, sc_cell = getattr(uc_cell, attr, None), getattr(sc_cell, attr)

    if isinstance(expected, dict):
        assert ui_cell is None or ui_cell != expected[engine]
        assert si_cell == expected[engine]
        assert uc_cell is None or uc_cell != expected[engine]
        assert sc_cell == expected[engine]
    else:
        assert ui_cell is None or ui_cell != expected
        assert si_cell == expected
        assert uc_cell is None or uc_cell != expected
        assert sc_cell == expected
